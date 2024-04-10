import pandas as pd

df = pd.read_csv('machine-readable-business-employment-data-dec-2023-quarter.csv')

# Convert 'Period' column to string data type
df['Period'] = df['Period'].astype(str)

# Extract year and month from 'Period' column
df['Year'] = df['Period'].str.split('.').str[0]
df['Month'] = df['Period'].str.split('.').str[1]

# Group by 'Series_reference', 'Year', and 'Month' and count occurrences of 'F' and 'R'
grouped = df.groupby(['Series_reference', 'Year', 'Month'])['STATUS'].value_counts().unstack().fillna(0)

# Reset index to convert the groupby result back to a DataFrame
grouped.reset_index(inplace=True)

# Sort the DataFrame first by 'Series_reference', then by 'Year', and finally by 'Month' within each year
grouped = grouped.sort_values(by=['Series_reference', 'Year', 'Month'])

print(grouped)
