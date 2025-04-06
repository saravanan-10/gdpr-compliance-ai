import os
import re
import json

def scan_file(file_path, rules):
    issues = []
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        code = file.read()

        if rules.get("cookie_consent_required") and "cookie" not in code.lower():
            issues.append("Missing cookie consent logic.")

        if "localStorage" in code or "sessionStorage" in code:
            issues.append("Potential personal data storage found.")

    return issues

def validate_code(repo_path, country):
    with open("data/country_rules.json") as f:
        country_rules = json.load(f)

    if country not in country_rules:
        print(f"No rules found for {country}")
        return

    rules = country_rules[country]
    issues_found = {}

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith((".js", ".py", ".php", ".html")):
                path = os.path.join(root, file)
                issues = scan_file(path, rules)
                if issues:
                    issues_found[path] = issues

    if issues_found:
        print("\nCompliance issues found:")
        for path, issues in issues_found.items():
            print(f"{path}:")
            for issue in issues:
                print(f"  - {issue}")
    else:
        print("Codebase is GDPR compliant for", country)