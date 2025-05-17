from google.adk.agents import Agent
# from google.adk.tools import google_search
from .prompt import instruction_prompt
from .tools import get_current_time, get_current_weather, calculate_tip

root_agent = Agent(
  name="adk_workshop_function_calling_agent",
  model="gemini-2.0-flash",
  description="A workshop demonstration agent that showcases ADK function calling capabilities.",
  instruction=instruction_prompt,
  tools=[get_current_time, get_current_weather, calculate_tip]
  # tools=[google_search]
)