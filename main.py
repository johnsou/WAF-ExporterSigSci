import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
email = os.getenv("SIGSCI_EMAIL")
api_token = os.getenv("SIGSCI_API_TOKEN")
corp = os.getenv("CORP_NAME")

# Auth headers
headers = {
    "x-api-user": email,
    "x-api-token": api_token,
    "accept": "application/json"
}

# Base URL
base_url = "https://dashboard.signalsciences.net/api/v0"

def get_sites():
    url = f"{base_url}/corps/{corp}/sites"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json().get("data", [])

def get_rules(site_name):
    url = f"{base_url}/corps/{corp}/sites/{site_name}/rules"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json().get("data", [])

def get_custom_rules(site_name):
    url = f"{base_url}/corps/{corp}/sites/{site_name}/custom-rules"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 404:
        return []  # Some sites might not have custom rules
    resp.raise_for_status()
    return resp.json().get("data", [])

def extract_all_rules():
    sites = get_sites()
    all_rules = []

    for site in sites:
        site_name = site["name"]
        print(f"Fetching rules for site: {site_name}")
        rules = get_rules(site_name)
        custom_rules = get_custom_rules(site_name)
        for rule in rules + custom_rules:
            rule["site"] = site_name
            all_rules.append(rule)

    return all_rules

# Extract and display or store
rules_data = extract_all_rules()

# Display summary
print(f"\nTotal rules extracted: {len(rules_data)}")
for r in rules_data[:5]:  # Show sample
    print(f"[{r['site']}] {r.get('type', '')} - {r.get('signal', '')} - {r.get('enabled', '')}")

# Optional: Save to JSON or CSV
import json
with open("all_rules.json", "w") as f:
    json.dump(rules_data, f, indent=2)
