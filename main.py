import argparse
from ingestion.fetch_gdpr_updates import fetch_gdpr_updates
from analysis.validate_code import validate_code
from ai.ai_compliance_assistant import suggest_fix, explain_rule

parser = argparse.ArgumentParser(description="GDPR Compliance AI System")
parser.add_argument("command", choices=["update", "validate", "suggest", "explain"])
parser.add_argument("--repo", help="Path to code repo for validation")
parser.add_argument("--country", help="Country to validate against")
parser.add_argument("--code", help="Code snippet for AI suggestion")
parser.add_argument("--rule", help="GDPR rule key to explain")

args = parser.parse_args()

if args.command == "update":
    fetch_gdpr_updates()

elif args.command == "validate":
    if not args.repo or not args.country:
        print("Usage: main.py validate --repo PATH --country COUNTRY")
    else:
        validate_code(args.repo, args.country)

elif args.command == "suggest":
    if args.code:
        print(suggest_fix(args.code))
    else:
        print("Usage: main.py suggest --code 'your code snippet'")

elif args.command == "explain":
    if args.country and args.rule:
        print(explain_rule(args.country, args.rule))
    else:
        print("Usage: main.py explain --country COUNTRY --rule RULE_KEY")