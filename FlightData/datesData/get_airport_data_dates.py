from serpapi import GoogleSearch
import json
import os
from dotenv import load_dotenv
import time
from datetime import datetime, timedelta

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")

def generate_params(outbound_date):
    params = {
        "api_key": api_key,
        "engine": "google_flights",
        "hl": "en",
        "gl": "us",
        "departure_id": "MIA",
        "arrival_id": "JFK",
        "outbound_date": outbound_date,
        "currency": "USD",
        "show_hidden": "true",
        "travel_class": "1",
        "type": 2
    }
    return params

def date_range(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)

if __name__ == "__main__":
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 7, 7)
    
    for date in date_range(start_date, end_date):
        date_str = date.strftime("%Y-%m-%d")
        results_file_name = f"{date_str}.json"
        params = generate_params(date_str)
        search = GoogleSearch(params)
        results = search.get_dict()
        
        with open(results_file_name, "w") as f:
            json.dump(results, f)