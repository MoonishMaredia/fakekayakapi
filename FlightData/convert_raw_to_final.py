import os
import json
from datetime import datetime
from dotenv import load_dotenv
import time

load_dotenv()

carry_on_fees = {
    'Spirit':[50]
}

checked_fees = {
    'Alaska':[35,45,150],
    'American':[35,45,150],
    'Delta':[35,45,150],
    'Frontier':[70, 90, 100],
    'Hawaiian':[25,40,100],
    'Jet Blue':[40,60,125],
    'Southwest':[0, 0, 125],
    'Spirit':[55, 80, 90]
}

airport_codes = {
    'ATL': {'city': 'Atlanta',
    'name': 'Atlanta Hartsfield International Airport'},
   'DFW': {'city': 'Dallas/Fort Worth',
    'name': 'Dallas/Fort Worth International Airport'},
   'DEN': {'city': 'Denver', 'name': 'Denver International Airport'},
   'LAX': {'city': 'Los Angeles', 'name': 'Los Angeles International Airport'},
   'ORD': {'city': 'Chicago', 'name': "O'Hare International Airport Airport"},
   'JFK': {'city': 'New York',
    'name': 'New York, John F Kennedy International Airport'},
   'MCO': {'city': 'Orlando', 'name': 'Orlando International Airport'},
   'LAS': {'city': 'Las Vegas',
    'name': 'Las Vegas, Las Vegas McCarran International Airport'},
   'CLT': {'city': 'Charlotte',
    'name': 'Charlotte/Douglas International Airport'},
   'MIA': {'city': 'Miami', 'name': 'Miami International Airport'},
   'SEA': {'city': 'Seattle', 'name': 'Seattle, Tacoma International Airport'},
   'EWR': {'city': 'Newark', 'name': 'Newark International Airport'},
   'SFO': {'city': 'San Francisco',
    'name': 'San Francisco International Airport'},
   'PHX': {'city': 'Phoenix',
    'name': 'Phoenix Sky Harbor International Airport'},
   'IAH': {'city': 'Houston',
    'name': 'Houston, George Bush Intercontinental Airport'},
   'BOS': {'city': 'Boston', 'name': 'Boston, Logan International Airport'},
   'FLL': {'city': 'Fort Lauderdale',
    'name': 'Fort Lauderdale-Hollywood International Airport'},
   'MSP': {'city': 'Minneapolis/St.Paul',
    'name': 'Minneapolis/St.Paul International Airport'},
   'LGA': {'city': 'New York', 'name': 'New York, La Guardia Airport'},
   'DTW': {'city': 'Detroit', 'name': 'Detroit Metropolitan Airport'},
   'PHL': {'city': 'Philadelphia', 'name': 'Philadelphia International Airport'},
   'SLC': {'city': 'Salt Lake City', 'name': 'Salt Lake City International Airport'},
   'BWI': {'city': 'Baltimore', 'name': 'Baltimore International Airport'},
   'DCA': {'city': 'Washington', 'name': 'Ronald Reagan Washington National Airport'},
   'SAN': {'city': 'San Diego', 'name': 'San Diego International Airport'},
   'IAD': {'city': 'Washington',
    'name': 'Washington, Dulles International Airport'},
   'TPA': {'city': 'Tampa', 'name': 'Tampa International Airport'},
   'BNA': {'city': 'Nashville', 'name': 'Nashville International Airport'},
   'AUS': {'city': 'Austin', 'name': 'Austin Bergstrom International Airport'},
   'MDW': {'city': 'Chicago', 'name': 'Chicago Midway Airport'},
   'HNL': {'city': 'Honolulu', 'name': 'Honolulu International Airport'},
   'DAL': {'city': 'Dallas', 'name': 'Dallas Love Field Airport'},
   'PDX': {'city': 'Portland', 'name': 'Portland International Airport'},
   'STL': {'city': 'St Louis',
    'name': 'St Louis, Lambert International Airport'},
   'RDU': {'city': 'Raleigh', 'name': 'Raleigh International Airport'},
   'HOU': {'city': 'Houston', 'name': 'Houston, William B Hobby Airport'},
   'SMF': {'city': 'Sacramento', 'name': 'Sacramento International Airport'},
   'MSY': {'city': 'New Orleans', 'name': 'New Orleans International Airport'},
   'SJC': {'city': 'San Jose', 'name': 'San Jose International Airport'},
   'SJU': {'city': 'San Juan', 'name': 'Luis Muñoz Marín International Airport'},
   'SNA': {'city': 'Santa Ana', 'name': 'John Wayne Airport'},
   'MCI': {'city': 'Kansas City', 'name': 'Kansas City International Airport'},
   'OAK': {'city': 'Oakland', 'name': 'Oakland International Airport'},
   'SAT': {'city': 'San Antonio', 'name': 'San Antonio International Airport'},
   'RSW': {'city': 'Fort Meyers', 'name': 'Southwest Florida International Airport'},
   'CLE': {'city': 'Cleveland', 'name': 'Cleveland Hopkins International Airport'},
   'IND': {'city': 'Indianapolis', 'name': 'Indianapolis International Airport'},
   'PIT': {'city': 'Pittsburgh', 'name': 'Pittsburgh International Airport'},
   'CVG': {'city': 'Cincinnati', 'name': 'Cincinnati International Airport'},
   'CMH': {'city': 'Columbus', 'name': 'John Glenn Columbus International Airport'},
   'PBI': {'city': 'West Palm Beach', 'name': 'Palm Beach International Airport'},
   'OGG': {'city': 'Kahului', 'name': 'Kahului Airport'},
   'JAX': {'city': 'Jacksonville', 'name': 'Jacksonville International Airport'},
   'ONT': {'city': 'Ontario', 'name': 'Ontario International Airport'},
   'BUR': {'city': 'Burbank', 'name': 'Hollywood Burbank Airport'},
   'BDL': {'city': 'Hartford', 'name': 'Bradley International Airport'},
   'CHS': {'city': 'Charleston', 'name': 'Charleston International Airport'},
   'MKE': {'city': 'Milwaukee', 'name': 'Milwaukee Mitchell International Airport'},
   'ANC': {'city': 'Anchorage', 'name': 'Anchorage International Airport'},
   'ABQ': {'city': 'Albuquerque', 'name': 'Albuquerque International Airport'},
   'OMA': {'city': 'Omaha', 'name': 'Eppley Airfield'},
   'MEM': {'city': 'Memphis', 'name': 'Memphis International Airport'},
   'RIC': {'city': 'Richmond', 'name': 'Richmond International Airport'},
   'BOI': {'city': 'Boise', 'name': 'Boise Airport'}}


date_time_str = '2024-09-15 20:10'

def get_hours_from_datetime(date_time_str):
    
    # Parse the date time string
    dt = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')

    # Extract the hours and minutes
    hours = dt.hour
    minutes = dt.minute

    # Convert to a number representing the time of day
    time_of_day = hours + (minutes / 60)
    
    return time_of_day

def convert_function(orig_code, dest_code):

    fileName = orig_code + "_" + dest_code + ".json"
    try:
        with open("./rawData/" + fileName) as f:
            data = json.load(f)
    except FileNotFoundError:
        # print(f"File {fileName} not found.")
        return []

    unique_key = orig_code + "_" + dest_code
    results = []

    isMissing = False

    try:
        priceLow = data['price_insights']['typical_price_range'][0]
        priceHigh = data['price_insights']['typical_price_range'][1]
        priceMid = (priceLow + priceHigh) / 2
        lower_25_range = (priceLow + priceMid) / 2
        upper_25_range = (priceHigh + priceMid) / 2
    except KeyError:
        isMissing = True

    for key in ['best_flights', 'other_flights']:
        if key not in data:
            continue
        for entry in data[key]:
            try:
                flights_item = entry['flights']
                layovers_item = entry.get('layovers', False)

                flight_dict = dict()

                flight_dict['travel_key'] = unique_key

                flight_dict['airline_logo'] = entry['airline_logo']

                flight_dict['trip_cost'] = entry['price']

                flight_dict['type'] = entry['type']

                flight_dict['total_duration'] = entry['total_duration']

                flight_dict['start_time'] = flights_item[0]['departure_airport']['time']

                flight_dict['start_time_hours'] = get_hours_from_datetime(flights_item[0]['departure_airport']['time'])

                flight_dict['end_time'] = flights_item[-1]['arrival_airport']['time']

                flight_dict['end_time_hours'] = get_hours_from_datetime(flights_item[-1]['arrival_airport']['time'])

                flight_dict['num_stops'] = len(flights_item) - 1

                if layovers_item:
                    flight_dict['layover'] = layovers_item
                else:
                    flight_dict['layover'] = None

                if not isMissing:
                    if flight_dict['trip_cost'] <= lower_25_range:
                        dealQuality = "Great Deal"
                    elif lower_25_range < flight_dict['trip_cost'] <= upper_25_range:
                        dealQuality = "Typical"
                    else:
                        dealQuality = "Pricier Than Usual"
                else:
                    dealQuality = "Not Available"

                flight_dict['deal_quality'] = dealQuality

                flightsArr = []

                airlineSet = set()
                for flightLeg in flights_item:
                    flightItem = dict()
                    flightItem['flight_number'] = flightLeg['flight_number']
                    flightItem['start_time'] = flightLeg['departure_airport']['time']
                    flightItem['end_time'] = flightLeg['arrival_airport']['time']
                    flightItem['start_airport'] = flightLeg['departure_airport']['id']
                    flightItem['end_airport'] = flightLeg['arrival_airport']['id']
                    flightItem['duration'] = flightLeg['duration']
                    flightItem['airplane'] = flightLeg.get('airplane', "Unavailable")
                    flightItem['airline'] = flightLeg['airline']
                    airlineSet.add(flightLeg['airline'])
                    flightsArr.append(flightItem)

                flight_dict['flights'] = flightsArr
                flight_dict['airline'] = airlineSet.pop() if len(airlineSet) == 1 else 'Multiple Airlines'

                results.append(flight_dict)
            except KeyError as e:
                # print(f"Missing key {e} in entry, skipping this entry.")
                continue

    return results
    
if __name__=="__main__":
     
    finalResult = []
    airportCodeKeys = list(airport_codes.keys())

    for departure in airportCodeKeys:
        for arrival in airportCodeKeys:
            if(departure==arrival): continue

            else:
                resultObj = convert_function(departure, arrival)
                finalResult.extend(resultObj)

    with open('output.txt', 'w') as filehandle:
        json.dump(finalResult, filehandle)


