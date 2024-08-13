import pandas as pd

# Load the CSV into a DataFrame
df = pd.read_csv('flight_prices.csv')

# Set the reference date for scaling
reference_date = '2024-09-15'

# Extract the mean price for the reference date
reference_mean_price = df.loc[df['Date'] == reference_date, 'Mean Price'].values[0]

# Scale the Mean Price and Std Dev Price relative to the reference date
df['Mean Scalar'] = df['Mean Price'] / reference_mean_price
df['Scaled Std Dev'] = df['Std Dev Price'] / reference_mean_price

# Save the scaled data to a new CSV file
df[['Date', 'Mean Scalar', 'Scaled Std Dev']].to_csv('scaled_flight_prices.csv', index=False)