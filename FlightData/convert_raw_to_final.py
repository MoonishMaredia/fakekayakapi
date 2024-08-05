import os
import json

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
    
        for entry in data[key]:    
            flights_item = entry['flights']
            layovers_item = entry.get('layovers', False)
            flight_dict = dict()
            flight_dict['airline_logo'] = entry['airline_logo']
            flight_dict['trip_cost'] = entry['price']
            flight_dict['type'] = entry['type']
            flight_dict['total_duration'] = entry['total_duration']
            flight_dict['start_time'] = flights_item[0]['departure_airport']['time']
            flight_dict['end_time'] = flights_item[-1]['arrival_airport']['time']
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
                flightItem[flightLeg['flight_number']] = dict()
                flightItem[flightLeg['flight_number']]['start_time'] = flightLeg['departure_airport']['time']
                flightItem[flightLeg['flight_number']]['end_time'] = flightLeg['arrival_airport']['time']
                flightItem[flightLeg['flight_number']]['start_airport'] = flightLeg['departure_airport']['id']
                flightItem[flightLeg['flight_number']]['end_airport'] = flightLeg['arrival_airport']['id']
                flightItem[flightLeg['flight_number']]['duration'] = flightLeg['duration']
                flightItem[flightLeg['flight_number']]['airplane'] = flightLeg['airplane']
                flightItem[flightLeg['flight_number']]['airline'] = flightLeg['airline']
                airlineSet.add(flightLeg['airline'])
                flightsArr.append(flightItem)
            
            flight_dict['flights'] = flightsArr
            if(len(airlineSet)==1): flight_dict['airline'] = airlineSet.pop()
            else: flight_dict['airline'] = 'Multiple Airlines'
            
        results.append(flight_dict)

        return results
    
if __name__=="__main__":
    print("something")
