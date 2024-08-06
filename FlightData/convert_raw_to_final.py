import os
import json
from datetime import datetime

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
    f = open(fileName)
    data = json.load(f)

    results = []

    priceLow = data['price_insights']['typical_price_range'][0]

    priceHigh = data['price_insights']['typical_price_range'][1]

    priceMid = (priceLow + priceHigh)/2

    lower_25_range = (priceLow +  priceMid)/2

    upper_25_range = (priceHigh +  priceMid)/2

    for key in ['best_flights','other_flights']:    
        print(len(data[key]))
        for entry in data[key]:
            
            flights_item = entry['flights']
            
            layovers_item = entry.get('layovers', False)
            
            flight_dict = dict()
            
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
                flight_dict['layover'] = entry['layovers']
            else:
                flight_dict['layover'] = None
                
            if(flight_dict['trip_cost'] <= lower_25_range):
                dealQuality = "Great Deal"
            elif(flight_dict['trip_cost'] > lower_25_range and flight_dict['trip_cost'] <= upper_25_range):
                dealQuality = "Typical"
            elif(flight_dict['trip_cost'] > upper_25_range):
                dealQuality = "Pricier Than Usual"
            else:
                dealQuality = "Not Available"
                
            flight_dict['deal_quality'] = dealQuality
            
            flightsArr = []
            
            for flightLeg in flights_item:
                airlineSet = set()
                flightItem = dict()
                flightItem['flight_number'] = flightLeg['flight_number']
                flightItem['start_time'] = flightLeg['departure_airport']['time']
                flightItem['end_time'] = flightLeg['arrival_airport']['time']
                flightItem['start_airport'] = flightLeg['departure_airport']['id']
                flightItem['end_airport'] = flightLeg['arrival_airport']['id']
                flightItem['duration'] = flightLeg['duration']
                flightItem['airplane'] = flightLeg['airplane']
                flightItem['airline'] = flightLeg['airline']
                airlineSet.add(flightLeg['airline'])
                flightsArr.append(flightItem)
                
            flight_dict['flights'] = flightsArr
            if(len(airlineSet)==1): flight_dict['airline'] = airlineSet.pop()
            else: flight_dict['airline'] = 'Multiple Airlines'
                
            results.append(flight_dict)

        return results
    
if __name__=="__main__":
    print("something")
