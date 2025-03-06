
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')
api_key=os.getenv('GOOGLE_API_KEY')


from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo

from agents.aiagents import fetch_fantasy_selector_agent,fetch_stats_agent,fetch_web_agent


import streamlit as st  
from phi.agent import Agent, RunResponse
st.title("🏏 AI-Powered Fantasy Cricket Team Selector")



# Match Details Input
match_details = st.text_input("Enter Match Details (Teams)", 
                              "UP Warriorz Women vs Mumbai Indians Women")

# Date Input
match_date = st.date_input("Select Match Date")


fantasy_team_agent = Agent(
    team=[fetch_web_agent(), fetch_stats_agent(), fetch_fantasy_selector_agent()],
    model=Gemini(api_key=api_key),
    instructions=["Provide the final team with reasoning for each selection.", "Use tables for better clarity."],
    markdown=True,
)


# Button to generate the fantasy team
if st.button("Generate Fantasy Team"):
    query = f"Select the best fantasy team for {match_details} on {match_date}."

    with st.spinner("Analyzing match data and selecting the best team..."):
        try:
            run: RunResponse = fantasy_team_agent.run(query)
            st.subheader("🏆 Recommended Fantasy Team")
            st.markdown(run.content)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")


