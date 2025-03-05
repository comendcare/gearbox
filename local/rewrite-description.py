import json
import time
from openai import OpenAI
from tqdm import tqdm  # Progress bar

# Set up OpenAI API key
client = OpenAI(api_key="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")

# File paths
input_file = "../data/input/fixedCombinedFinalData.json"
output_file = "../data/output/fixedCombinedFinalDataNewDescriptions.json"

# Load input JSON data
with open(input_file, "r", encoding="utf-8") as f:
    companies = json.load(f)

# Try to resume from an existing output file if it exists
try:
    with open(output_file, "r", encoding="utf-8") as f:
        processed_companies = json.load(f)
    processed_titles = {company["title"] for company in processed_companies}
except (FileNotFoundError, json.JSONDecodeError):
    processed_companies = []
    processed_titles = set()

def generate_description(company):
    """Generate an improved description using OpenAI API, with a fallback to the original."""
    prompt = f"""
    Given the following structured data about a company, rewrite the description to be informative and natural while preserving its meaning and unique quality. Write in third person objective. Keep it between 50 and 150 words. Remove ANY mention of scientist.com in any capacity. Normalize for new lines and any formatting, but keep things like trademarks, acronyms, or anything that preserves the unique quality of the description.

    Company Name: {company.get('title', 'Unknown')}

    Sites:
    {', '.join([site['address'] for site in company.get('sites', []) if 'address' in site])}

    Services:
    {', '.join([service['name'] for service in company.get('services', []) if 'name' in service])}

    Certifications:
    {', '.join([cert['name'] for cert in company.get('certifications', []) if 'name' in cert])}

    Original Description: 
    {company.get('description', '')}

    ---
    Improved Description:
    """

    try:
        start_time = time.time()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a professional business content writer."},
                      {"role": "user", "content": prompt}],
            temperature=0.7
        )
        end_time = time.time()
        return response.choices[0].message.content.strip(), end_time - start_time
    except Exception as e:
        print(f"Error processing {company.get('title', 'Unknown')}: {e}")
        return company.get("description", ""), 0  # Fallback to original description

# Process each company and write results immediately
remaining_companies = [c for c in companies if c["title"] not in processed_titles]
total_companies = len(remaining_companies)

if total_companies == 0:
    print("All companies have already been processed.")
else:
    print(f"Processing {total_companies} companies...")

    with open(output_file, "w", encoding="utf-8") as f:
        processing_times = []
        progress_bar = tqdm(remaining_companies, desc="Processing companies", unit="company")

        for i, company in enumerate(progress_bar):
            start_loop = time.time()
            company["description"], process_time = generate_description(company)

            # Track processing times
            processing_times.append(process_time)
            avg_time = sum(processing_times) / len(processing_times) if processing_times else 1
            remaining_time = avg_time * (total_companies - (i + 1))

            # Update progress bar with estimated time
            progress_bar.set_postfix({
                "ETA (s)": f"{remaining_time:.1f}",
                "Avg Time (s)": f"{avg_time:.2f}"
            })

            # Write each company as it's processed
            processed_companies.append(company)
            f.seek(0)  # Move to beginning of file
            json.dump(processed_companies, f, indent=2, ensure_ascii=False)
            f.flush()  # Ensure immediate write to disk

            time.sleep(1)  # Rate limit buffer

    print("\nUpdated descriptions saved to:", output_file)
