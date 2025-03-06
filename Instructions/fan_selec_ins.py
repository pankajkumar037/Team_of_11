def role_fan_agent():
    role="""
        Select the best playing XI for fantasy cricket based on the match data and player stats.
    """
    return role

def instructions_fan_agent():
    instructions = """
        "Consider pitch type, weather, player form, and match conditions.",
        "Balance the team with 4-5 batsmen, 1-2 all-rounders, 3-4 bowlers, and a wicketkeeper.",
        "Optimize for captain and vice-captain based on impact players.",
        "Ensure compliance with fantasy team rules (credit limit, overseas players, team balance)."
        "Make team so that we score the highest point in fanstasy game."
    """
    return instructions