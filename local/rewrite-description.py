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
        response = client.chat.completions.create(model="gpt-4",
        messages=[{"role": "system", "content": "You are a professional business content writer."},
                  {"role": "user", "content": prompt}],
        temperature=0.7)
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error processing {company.get('title', 'Unknown')}: {e}")
        return company.get("description", "")  # Fallback to the original description


def generate_services(company, predefined_services):
    """Generate a refined list of services from a predefined list based on the company's description and existing services."""
    prompt = f"""
    Given the following structured data about a company, identify and select the most relevant services from the predefined list.
    The goal is to ensure accuracy and consistency in service categorization while maintaining a natural and informative structure.

    Company Name: {company.get('title', 'Unknown')}
    Year Established: {company.get('yearEstablished', 'Unknown')}
    Headquarters: {company.get('headquarters', 'Unknown')}
    Company Type: {company.get('companyType', 'Unknown')}

    Sites:
    {', '.join([site['address'] for site in company.get('sites', []) if 'address' in site])}

    Existing Services:
    {', '.join([service['name'] for service in company.get('services', []) if 'name' in service])}

    Certifications:
    {', '.join([cert['name'] for cert in company.get('certifications', []) if 'name' in cert])}

    Company Description: 
    {company.get('description', '')}

    Predefined Services List:
    {', '.join(predefined_services)}

    Select the most relevant services from the predefined list based on the company's description and existing services. Return the response as a comma-separated list.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in business categorization and taxonomy."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        selected_services = response.choices[0].message.content.strip()

        # Convert response to list format
        selected_services_list = [service.strip() for service in selected_services.split(',') if
                                  service.strip() in predefined_services]

        return selected_services_list
    except Exception as e:
        print(f"Error processing {company.get('title', 'Unknown')}: {e}")
        return [service['name'] for service in company.get('services', []) if
                'name' in service]  # Fallback to existing services


# Process each company and write results immediately
with open(output_file, "w", encoding="utf-8") as f:
    for company in companies:
        if company["title"] in processed_titles:
            print(f"Skipping already processed: {company['title']}")
            continue

        print(f"Processing: {company['title']}")
        company["description"] = generate_description(company)
        # company["comendServices"] = generate_services(company, ["service1", "service2", "service3", "service4", "service5"])

        # Write each company as it's processed
        processed_companies.append(company)
        f.seek(0)  # Move to beginning of file
        json.dump(processed_companies, f, indent=2, ensure_ascii=False)
        f.flush()  # Ensure immediate write to disk

        time.sleep(1)  # Rate limit buffer

print("Updated descriptions saved to:", output_file)
