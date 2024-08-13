import pandas as pd
import json


if __name__ == "__main__":
    stats_df = pd.read_csv('scaled_flight_prices_final.csv')
    finalDict = {}
    for index, row in stats_df.iterrows():
        key = str(row['month']) + "_" + str(row['day'])
        finalDict[key] = [row['mean_scalar'], row['std_dev']]

    with open('flight_scalars.json', 'w') as json_file:
        json.dump(finalDict, json_file, indent=4)
    