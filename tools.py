import requests
from datetime import datetime
import json

class Tools:
    @staticmethod
    def get_weather(city="Delhi"):
        """मौसम बताता है"""
        try:
            url = f"https://wttr.in/{city}?format=%C+%t+%w"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return f"🌤️ {city} में मौसम: {response.text.strip()}"
            return "Weather information नहीं मिली"
        except:
            return "Weather API में error आया"

    @staticmethod
    def get_time():
        """समय बताता है"""
        now = datetime.now()
        return f"🕒 अभी समय है: {now.strftime('%I:%M %p')}"

    @staticmethod
    def wikipedia_search(query):
        """Wikipedia से जानकारी लाता है"""
        try:
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                return f"📖 {data.get('extract', 'Information नहीं मिली')}"
            return "Wikipedia से जानकारी नहीं मिली"
        except:
            return "Search में error आया"

    @staticmethod
    def calculator(expression):
        """Simple calculator"""
        try:
            result = eval(expression)
            return f"🧮 {expression} = {result}"
        except:
            return "Calculation error"

# Tool definitions for LLM
available_tools = {
    "get_weather": Tools.get_weather,
    "get_time": Tools.get_time,
    "wikipedia_search": Tools.wikipedia_search,
    "calculator": Tools.calculator
}