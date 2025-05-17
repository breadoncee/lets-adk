from google.adk.agents import Agent
from ..prompts import quote_agent_prompt

quote_agent = Agent(
  name="quote_agent",
  model="gemini-2.0-flash",
  description="A motivational quote agent. Your only task is to respond with short, uplifting, or inspiring quotes to encourage or motivate the user.",
  instruction=quote_agent_prompt,
)