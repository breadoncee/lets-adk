from google.adk.agents import LlmAgent
from .prompt import action_recommender_prompt

action_recommender_agent = LlmAgent(
  name="ActionRecommenderAgent",
  model="gemini-2.0-flash",
  description="Recommend actions to fix a bug.",
  instruction=action_recommender_prompt,
  output_key="action_recommendations",
)