from google.adk.agents import SequentialAgent
from .sub_agents import bug_type_agent, bug_severity_agent, action_recommender_agent, bug_summary_agent

bug_classifier_agent = SequentialAgent(
  name="BugClassifierPipeline",
  description="Execute a sequence of sub-agents to classify a bug. This is going to be a bug report from the react web application named DevTools.",
  sub_agents=[
    bug_type_agent,
    bug_severity_agent,
    action_recommender_agent,
    bug_summary_agent,
  ],
)

root_agent = bug_classifier_agent
