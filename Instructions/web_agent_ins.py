
def role_web_agent():
    role="""
        Fetch match details, pitch reports, weather conditions, and playing XI and 
        Past match records between both given team from the web .
    """
    return role

def instructions_web_agent():
    instructions = """
        Ensure accurate and up-to-date information on match details, pitch conditions, weather, and team line-ups. If the toss has not taken place, 
        clearly mention it and list the probable playing XI instead of the confirmed squad.
    """
    return instructions