import aiohttp
from typing import Dict
import asyncio

async def get_current_weather(city: str) -> Dict:
    """
    Get current weather conditions for any location worldwide.
    
    This function fetches real-time weather data including temperature, conditions, 
    wind information, and more. Use this to provide up-to-date weather information 
    when users ask about current weather conditions.

    Args:
        city: The city name or coordinates to fetch weather for.

    Returns:
        A structured dictionary containing formatted weather data ready for ADK function tools.
    """
    base_url = "http://api.weatherapi.com/v1/current.json"
    api_key = "74158128634a43b9b0b234901251605"

    params = {
        "key": api_key,
        "q": city
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(base_url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                
                # Adding a 5-second delay to simulate a long-running function
                await asyncio.sleep(5)
                
                return {
                    "status": "Success",
                    "location": data["location"]["name"],
                    "country": data["location"]["country"],
                    "temperature_c": data["current"]["temp_c"],
                    "temperature_f": data["current"]["temp_f"],
                    "condition": data["current"]["condition"]["text"],
                    "wind_speed": data["current"]["wind_kph"],
                    "wind_direction": data["current"]["wind_dir"],
                    "humidity": data["current"]["humidity"],
                    "feels_like_c": data["current"]["feelslike_c"],
                    "feels_like_f": data["current"]["feelslike_f"],
                    "last_updated": data["current"]["last_updated"]
                }
            else:
                error_text = await response.text()
                
                # Adding a 5-second delay to simulate a long-running function
                await asyncio.sleep(5)
                
                return {
                    "status": "Error",
                    "error_message": error_text
                }