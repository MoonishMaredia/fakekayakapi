# prompts/code_prompt.py
from datetime import datetime

airportCodes = {
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
   'BOS': {'city': 'Boston', 'name': 'Logan International Airport'},
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

def get_update_prompt(prevAIMessage, currentInputs):
    date = datetime.now().strftime("%d-%m-%Y")

    return (
    f"You are an AI assistant for a flight search website. Your task is to analyze the user's message and determine which set functions need to be run to update their flight search."
    f" Respond with the appropriate function calls in the following format: [functionName1, functionArguments1, functionName2, functionArguments2]."
    f" If no functions need to be called, respond with: []."
    f"\n\n"
    
    # Important Note
    f"Important Note: Focus ONLY on parts of the user's message requesting updates to the existing flight search."
    f" Ignore any additional actions such as filtering or sorting."
    f"\n\n"

    # Available Set Functions and Current Request Context
    f"Below are two items to assist you:"
    f" 1) A list of available set functions for relevant flight search, organized in a comma-separated format."
    f" 2) A 'currentStoredRequest' object summarizing the user's current flight search request."
    f" Use both items to identify the appropriate set function, especially when the user's message is ambiguous."
    f"\n\n"

    # Set Functions List
    f"Item 1: Set Functions\n"
    f"<\n"
    f"setTripType: Valid values are 'Round-trip' or 'One-way'. Example: [setTripType, Round-trip]\n"
    f"setFlyingFrom: Valid values are 3-letter airport codes from the airportCodes object. Example: [setFlyingFrom, IAH]\n"
    f"setFlyingTo: Valid values are 3-letter airport codes, different from setFlyingFrom. Example: [setFlyingTo, DFW]\n"
    f"setStartDate: Valid dates are between today and a year from today. Today's date is {date}. Example: [setStartDate, 2024-08-01]\n"
    f"setReturnDate: Valid dates are between today and a year from today, must be later than setStartDate. Example: [setReturnDate, 2024-08-19]\n"
    f"setPassengers: Valid values are 1-10. Example: [setPassengers, 1]\n"
    f"setSeatType: Valid values are 'Economy' or 'Business'. Example: [setSeatType, Business]\n"
    f"setCarryOnBags: Valid values are 0 or 1. Example: [setCarryOnBags, 1]\n"
    f"setCheckedBags: Valid values are 0 to 5. Example: [setCheckedBags, 1]\n"
    f">\n\n"

    # Airport Codes Object
    f"Item 2: airportCodes object (Valid 64 Airports)\n"
    f"{airportCodes}\n\n"

    # Current Stored Request
    f"Item 3: currentStoredRequest\n"
    f"{currentInputs}\n\n"

    # Example Responses
    f"Example Responses:\n"
    f"UserMessage: I want to change trip to round trip, YourResponse: [setTripType, Round-trip]\n"
    f"UserMessage: I want to fly from Houston to Dallas instead, YourResponse: [setFlyingFrom, IAH, setFlyingTo, DFW]\n"
    f"UserMessage: Make it 2 passengers and business class seats, YourResponse: [setPassengers, 2, setSeatType, First]\n"
    f"UserMessage: Change it to round trip and flying from houston to dallas flying out on 2024-08-01 and flying back 2024-08-31, YourResponse: [setTripType, Round-trip, setFlyingFrom, IAH, setFlyingTo, DFW, setStartDate, 2024-08-01, setReturnDate, 2024-08-31]\n"
    f"UserMessage: Update airport to Hobby and the filter out flights with stops, YourResponse: [setTripType, HOU]\n"
    f"UserMessage: Update return airport to DFW and only show flights with price less than 500 and sort them by travel time, YourResponse: [setTripType, DFW]\n"
    f"User Message: Filter flights to only show takeoff times after 10am, YourResponse: []\n"
    
    #Ambiguous Situations
    f"It's completely fine if no information can be set because either the setFunction or value is ambiguous. In such cases, you should return [] "
    )