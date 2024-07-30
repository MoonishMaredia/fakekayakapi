from serpapi import GoogleSearch
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("SERPAPI_KEY")

params = {
  "api_key": api_key,
  "engine": "google_flights",
  "hl": "en",
  "gl": "us",
  "departure_id": "MIA",
  "arrival_id": "JFK",
  "outbound_date": "2024-09-15",
  "return_date": "2024-09-30",
  "currency": "USD",
  "show_hidden": "true",
  "travel_class": "1"
}


search = GoogleSearch(params)
results = search.get_dict()

with open("apiTestData.json", "w") as f:
  json.dump(results, f)