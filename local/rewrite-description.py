import json
from openai import OpenAI

client = OpenAI(api_key="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")
import time


# Set up OpenAI API key

# Load input JSON data
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
    Given the following structured data about a company, rewrite the description to be more engaging, informative, and natural while preserving its meaning. Keep it under 250 words.

    Company Name: {company.get('title', 'Unknown')}
    Year Established: {company.get('yearEstablished', 'Unknown')}
    Headquarters: {company.get('headquarters', 'Unknown')}
    Company Type: {company.get('companyType', 'Unknown')}

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
        response = client.chat.completions.create(model="gpt-4",
        messages=[{"role": "system", "content": "You are a professional business content writer."},
                  {"role": "user", "content": prompt}],
        temperature=0.7)
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error processing {company.get('title', 'Unknown')}: {e}")
        return company.get("description", "")  # Fallback to the original description


# Process each company and write results immediately
with open(output_file, "w", encoding="utf-8") as f:
    for company in companies:
        if company["title"] in processed_titles:
            print(f"Skipping already processed: {company['title']}")
            continue

        print(f"Processing: {company['title']}")
        company["description"] = generate_description(company)

        # Write each company as it's processed
        processed_companies.append(company)
        f.seek(0)  # Move to beginning of file
        json.dump(processed_companies, f, indent=2, ensure_ascii=False)
        f.flush()  # Ensure immediate write to disk

        time.sleep(1)  # Rate limit buffer

print("Updated descriptions saved to:", output_file)
