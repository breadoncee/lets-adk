from google.adk.agents import LlmAgent
from .prompt import bug_type_prompt

bug_type_agent = LlmAgent(
  name="BugTypeClassifierAgent",
  model="gemini-2.0-flash",
  description="Classify bugs into categories.",
  instruction=bug_type_prompt,
  output_key="bug_type",
)
