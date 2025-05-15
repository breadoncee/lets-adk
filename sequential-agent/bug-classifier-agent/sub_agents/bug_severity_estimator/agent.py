from google.adk.agents import LlmAgent
from .prompt import bug_severity_estimator_prompt

bug_severity_agent = LlmAgent(
  name="BugSeverityEstimatorAgent",
  model="gemini-2.0-flash",
  description="Estimate the severity of a bug.",
  instruction=bug_severity_estimator_prompt,
  output_key="bug_severity",
)
