import pandas as pd

# Load the combined dataset
combined_csv_path = '/Users/gemma.p/Desktop/Co-op/HOOPP_interview/combined_parking_tickets.csv'
df = pd.read_csv(combined_csv_path, usecols=['date_of_infraction', 'infraction_code', 'infraction_description', 'set_fine_amount', 'location2'])

# Convert date_of_infraction to datetime and extract year
df['date_of_infraction'] = pd.to_datetime(df['date_of_infraction'], format='%Y%m%d')
df['year'] = df['date_of_infraction'].dt.year

# Aggregate data
df_aggregated = df.groupby(['year', 'infraction_code', 'infraction_description', 'location2']).agg({
    'set_fine_amount': 'sum',
    'date_of_infraction': 'count'
}).reset_index()

# Rename columns for clarity
df_aggregated.columns = ['Year', 'Infraction_Code', 'Infraction_Description', 'Location', 'Total_Fine_Amount', 'Ticket_Count']

# Save the processed data to a new CSV file
processed_csv_path = '/Users/gemma.p/Desktop/Co-op/HOOPP_interview/processed_parking_tickets.csv'
df_aggregated.to_csv(processed_csv_path, index=False)

print(f'Processed data saved to {processed_csv_path}')
