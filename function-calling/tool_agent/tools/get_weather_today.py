
def get_weather_today(location: str = "San Francisco") -> dict:
  """Get the current weather for a specific location."""
  # This is a mock function - in a real app, you'd call a weather API
  weather_data = {
    "San Francisco": "foggy, 65°F",
    "New York": "rainy, 72°F",
    "London": "cloudy, 60°F",
    "Tokyo": "sunny, 78°F"
  }
  return {
    "location": location,
    "weather": weather_data.get(location, "unknown")
  }