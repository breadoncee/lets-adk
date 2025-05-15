from google.adk.agents import LlmAgent
from .prompt import bug_summary_prompt

bug_summary_agent = LlmAgent(
  name="BugSummaryAgent",
  model="gemini-2.0-flash",
  description="Summarize a bug.",
  instruction=bug_summary_prompt,
  output_key="bug_summary",
)