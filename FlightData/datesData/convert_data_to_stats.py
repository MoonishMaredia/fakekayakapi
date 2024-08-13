import json
import csv
import os
from datetime import datetime, timedelta
import statistics

def date_range(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)

def get_flight_prices(flights):
    prices = []
    for flight in flights:
        try:
            price = flight["price"]
            if price is not None:
                prices.append(price)
        except KeyError:
            # Skip if price is not available
            continue
    return prices

def process_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Get prices from best_flights and other_flights
    best_flight_prices = get_flight_prices(data.get("best_flights", []))
    other_flight_prices = get_flight_prices(data.get("other_flights", []))

    # Combine prices from both best_flights and other_flights
    all_prices = best_flight_prices + other_flight_prices

    if all_prices:
        mean_price = statistics.mean(all_prices)
        variance_price = statistics.stdev(all_prices)
        return mean_price, variance_price
    else:
        return None, None

if __name__ == "__main__":
    finalDict = {}
    start_date = datetime(2024, 8, 20)
    end_date = datetime(2025, 7, 7)
    
    for date in date_range(start_date, end_date):
        date_str = date.strftime("%Y-%m-%d")
        file_name = f"{date_str}.json"
        
        if os.path.exists(file_name):
            mean_price, stdev_price = process_json_file(file_name)
            if mean_price is not None and stdev_price is not None:
                finalDict[date_str] = [mean_price, stdev_price]
            else:
                print(f"{date_str}: No valid prices found.")
        else:
            print(f"{date_str}: File not found.")

    # Store in JSON format
    with open('flight_prices.json', 'w') as json_file:
        json.dump(finalDict, json_file, indent=4)

# Store in CSV format
    with open('flight_prices.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Date', 'Mean Price', 'Std Dev Price'])  # Write header
        for date, stats in finalDict.items():
            writer.writerow([date] + stats)

    
