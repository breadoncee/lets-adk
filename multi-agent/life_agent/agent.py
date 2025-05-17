from google.adk.agents import Agent
from .prompts import personal_life_assistant_prompt
from .sub_agents import quote_agent, mood_check_agent, fun_fact_agent

root_agent = Agent(
  name="your_personal_life_agent",
  model="gemini-2.0-flash",
  description="A personal life agent that can help you with your daily life",
  instruction=personal_life_assistant_prompt,
  sub_agents=[
    quote_agent,
    mood_check_agent,
    fun_fact_agent
  ]
)