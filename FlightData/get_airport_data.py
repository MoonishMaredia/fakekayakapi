from serpapi import GoogleSearch
import json
import os
from dotenv import load_dotenv

load_dotenv()

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

api_key=os.getenv("SERPAPI_KEY")

def generate_params(departue_airport, arrival_airport):
  params = {
    "api_key": api_key,
    "engine": "google_flights",
    "hl": "en",
    "gl": "us",
    "departure_id": departue_airport,
    "arrival_id": arrival_airport,
    "outbound_date": "2024-09-15",
    "return_date": "2024-09-30",
    "currency": "USD",
    "show_hidden": "true",
    "travel_class": "1"
  }
  
  return params

if __name__=="__main__":
  airportCodeKeys = list(airport_codes.keys())[0:3]
  print(airportCodeKeys)
  for departure in airportCodeKeys:
    for arrival in airportCodeKeys:
      if(departure==arrival):
        continue
      else:
        params = generate_params(departure, arrival)
        search = GoogleSearch(params)
        results = search.get_dict()
        results_file_name = departure + "_" + arrival + ".json"
        with open(results_file_name, "w") as f:
          json.dump(results, f)