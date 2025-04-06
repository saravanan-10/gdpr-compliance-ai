def suggest_fix(code_snippet):
    # Simulated suggestion
    if "cookie" not in code_snippet.lower():
        return "Consider adding a cookie consent banner using Cookiebot or similar."
    return "Looks good!"

def explain_rule(country, rule_key):
    explanations = {
        "cookie_consent_required": "The site must obtain user consent before storing cookies.",
        "data_retention_max_months": "User data should not be stored beyond the allowed retention period."
    }
    return explanations.get(rule_key, "No description available.")