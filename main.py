import pandas as pd

# Read inventory in and out CSV files using pandas
inventory_in_df = pd.read_csv('inventory_in.csv')
inventory_out_df = pd.read_csv('inventory_out.csv')

# Concatenate incoming and outgoing inventory data
inventory_df = pd.concat([inventory_in_df, inventory_out_df])

# Convert date column to datetime
inventory_df['Date'] = pd.to_datetime(inventory_df['Date'])

# Extract year and month from the date column
inventory_df['Year'] = inventory_df['Date'].dt.year
inventory_df['Month'] = inventory_df['Date'].dt.month

# Sort the DataFrame by year in descending order and by month in ascending order
inventory_df.sort_values(by=['Year', 'Month'], ascending=[False, True], inplace=True)

# Format the date to display only the year and month
inventory_df['Date'] = inventory_df['Date'].dt.strftime('%Y-%m')

# Group the data by warehouse, year, and month, then sum the quantities
stock_movements = inventory_df.groupby(['Warehouse', 'Year', 'Month', 'Date'])['Quantity'].sum().unstack(fill_value=0)

# Reset index to move Year, Month, and Date back to columns
stock_movements.reset_index(inplace=True)

# Save results to CSV
stock_movements.to_csv('stock_movements.csv', index=False)
