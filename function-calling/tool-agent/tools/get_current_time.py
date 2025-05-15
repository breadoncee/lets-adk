from datetime import datetime

def get_current_time() -> dict:
  """Get the current date and time."""
  return {
    "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  }
  