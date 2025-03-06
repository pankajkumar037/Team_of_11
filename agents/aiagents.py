import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')
api_key=os.getenv('GOOGLE_API_KEY')

from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo


import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from instruction.web_agent_ins import instructions_web_agent,role_web_agent
from instruction.stat_agent_ins import instructions_stat_agent, role_stat_agent
from instruction.fan_selec_ins import instructions_fan_agent,role_fan_agent

# Agent to fetch match details, pitch report, and weather conditions
def fetch_web_agent():
    web_agent = Agent(
        name="Cricket Web Agent",
        role=role_web_agent(),
        model=Gemini(api_key=api_key),
        tools=[DuckDuckGo()],
        instructions=instructions_web_agent(),
        markdown=True,
    )
    return web_agent

# Agent to fetch player performance data
def fetch_stats_agent():
    stats_agent = Agent(
        name="Cricket Stats Agent",
        role=role_stat_agent(),
        model=Gemini(api_key=api_key),
        tools=[DuckDuckGo()],  
        instructions=instructions_stat_agent(),
        markdown=True,
    )
    return stats_agent

# Agent to create the best fantasy team
def fetch_fantasy_selector_agent():
    fantasy_selector = Agent(
        name="Fantasy Team Selector",
        role=role_fan_agent(),
        model=Gemini(api_key=api_key),
        instructions=instructions_fan_agent(),
        reasoning=True,
        markdown=True,
    )
    return fantasy_selector


