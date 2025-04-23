import pandas as pd
import os

# Set the folder path where your CSVs are stored
folder_path = 'csv'

# Change this if your join key column has a different name
join_column = 'name'  

# Get all CSV files in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Iterate through csv's and join them
merged_df = None

for file in csv_files:
    df = pd.read_csv(folder_path+'/'+file, encoding='utf-16', skiprows=2)
    df.columns.values[1] = file.replace('.csv','')
    
    if merged_df is None:
        merged_df = df  # First file sets the base
    else:
        merged_df = pd.merge(merged_df, df, on='Date', how='outer')

merged_df.to_csv('merged_df.csv', index=False)