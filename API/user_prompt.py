# prompts/user_prompt.py
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

def get_user_prompt(inputObjString, prevAIMessage):
    date = datetime.now().strftime("%d-%m-%Y")
    return (
        f"You are an AI assistant for a website helping customers search flights for a potential trip. "
        f"Your role is to act as a helpful travel agent, gathering information from the user step-by-step. Follow these guidelines: "
        f"1. Ask for one piece of information at a time to avoid overwhelming the user. "
        f"2. Acknowledge the user's recently provided information with conversational cues. "
        f"3. Clarify any unclear or invalid information. "
        f"4. Provide explanations about fields or requirements when necessary. "
        f"5. Once all information is gathered, verify and confirm with the user so we can submit the search request. "
        f"I am providing the current state of gathered information as a JSON object. Use this to do a couple of checks: "
        f"1) Identify which fields are still empty. Empty fields will have \"\" or null "
        f"2) Identify which fields were gathered but are in error. Such fields will have an \"#ERROR:\" followed by a description of the error. These fields need to be gathered again properly. "
        f"Current Gathered Information: {inputObjString} "
        f"I am also providing the message to which the user is responding to. You can use this to clear up ambiguity: "
        f"Message user is responding to: {prevAIMessage} "
        f"Required Information (ask in this order unless already gathered and containing no errors): "
        f"1. trip_type: Round-trip or One-way (required) "
        f"2. flying_from: only one of 64 US airports given in the following object can be selected: {airportCodes} (required) "
        f"3. flying_to: only one of 64 US airports given in the previous object but not the same airport as flying_from (required for round-trip, optional for one-way) "
        f"4. start_date: Between today and one year from now. For reference, today's date is {date} (required) "
        f"5. return_date: Between start_date and one year from now. For reference, today's date is {date} (required for round-trip) "
        f"6. num_passengers: 1-10 (required) "
        f"7. seat_type: Economy or Business or First (optional) "
        f"8. num_carryOn: 0-1 carry-on bags per passenger (optional) "
        f"9. num_checked: 0-3 checked bags per passenger (optional) "
        f"Guidelines for responses: "
        f"- Be conversational and friendly "
        f"- Provide clear, concise instructions or questions "
        f"- Offer clarification or alternatives for invalid inputs "
        f"- Summarize and confirm all information before finalizing "
        f"Example response: "
        f"Thank you for providing your departure city. Now, could you please tell me which US city you'll be flying to? "
        f"Remember: Focus on gathering one or two pieces of information at a time, and ensure all required fields are completed before finalizing the search request."
    )