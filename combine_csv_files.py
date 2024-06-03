import pandas as pd
import os

# Define the base directory where your CSV files are located
base_dir = '/Users/gemma.p/Desktop/Co-op/HOOPP_interview/'

# Define subdirectories for each year
subdirectories = [
    'parking-tickets-2017',
    'parking-tickets-2018',
    'parking-tickets-2019',
    'parking-tickets-2020'
]

# List to store individual dataframes
dataframes = []

# Loop through each subdirectory and read CSV files
for subdirectory in subdirectories:
    dir_path = os.path.join(base_dir, subdirectory)
    for filename in os.listdir(dir_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(dir_path, filename)
            df = pd.read_csv(file_path)
            dataframes.append(df)

# Combine all dataframes into a single dataframe
combined_df = pd.concat(dataframes, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_csv_path = os.path.join(base_dir, 'combined_parking_tickets.csv')
combined_df.to_csv(combined_csv_path, index=False)

print(f'Combined CSV saved to {combined_csv_path}')
