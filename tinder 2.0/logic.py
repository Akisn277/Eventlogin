# Sample data
startups = [
    {"id": 1, "name": "A", "industry": "Tech", "funding_req": 1000002, "req_skills": ["Python", "AI"]},
    {"id": 2, "name": "B", "industry": "Healthcare", "funding_req": 20001, "req_skills": ["Data Analysis"]},
]

skilled_individuals = [
    {"id": 1, "name": "Ak", "skills": ["Python", "AI", "ML"], "pref_indust": ["Tech", "Finance"]},
    {"id": 2, "name": "Indu", "skills": ["Data Analysis", "Healthcare"], "pref_indust": ["Healthcare"]},
]

investors = [
    {"id": 1, "name": "XYZ", "indust_pref": ["Tech"], "budget": 10},
    {"id": 2, "name": "UVW", "indust_pref": ["Healthcare", "Tech"], "budget": 40},
]

# Matching function
def match_profiles(startups, skilled_individuals, investors):
    matches = []
    
    for startup in startups:
        # Match with skilled individuals
        for individual in skilled_individuals:
            skill_match = len(set(startup["req_skills"]) & set(individual["skills"]))  # Common skills
            indust_match = startup["industry"] in individual["pref_indust"]  # Industry match
            
            if skill_match > 0 and indust_match:
                matches.append({
                    "type": "Startup-Skilled Match",
                    "startup": startup["name"],
                    "individual": individual["name"],
                    "score": skill_match  # Higher score = better match
                })
        
        # Match with investors
        for investor in investors:
            indust_match = startup["industry"] in investor["indust_pref"]  # Industry match
            funding_match = startup["funding_req"] <= investor["budget"]  # Funding within budget
            
            if indust_match and funding_match:
                matches.append({
                    "type": "Startup-Investor Match",
                    "startup": startup["name"],
                    "investor": investor["name"],
                    "score": startup["funding_req"] / investor["budget"]  # Lower ratio = better match
                })
    
    return matches

# Run the function
matches = match_profiles(startups, skilled_individuals, investors)

# Print matches
for match in matches:
    print(f"Match Type: {match['type']}")
    print(f"  Startup: {match['startup']}")
    if match['type'] == "Startup-Skilled Match":
        print(f"  Skilled Individual: {match['individual']}")
    elif match['type'] == "Startup-Investor Match":
        print(f"  Investor: {match['investor']}")
    print(f"  Match Score: {match['score']:.2f}")
    print()
