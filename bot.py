import requests
from datetime import datetime

# Get weather
weather = requests.get("https://wttr.in/?format=3").text

# Get quote
quote_data = requests.get("https://zenquotes.io/api/random").json()

quote = quote_data[0]["q"]
author = quote_data[0]["a"]

# Current date and time
today = datetime.now()

# Create summary
summary = f"""
Daily Pulse Report
==================

Date: {today}

Weather:
{weather}

Motivational Quote:
"{quote}"
- {author}
"""

# Save to file
with open("daily_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)

print("✅ Daily summary saved successfully!")