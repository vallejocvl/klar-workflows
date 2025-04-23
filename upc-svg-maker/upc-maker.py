import pandas as pd
import barcode

# Load my data
df = pd.read_csv('database/database.csv')

# Get barcode class
UPC = barcode.get_barcode_class('upc')

# Loop through my df and get item_name and upc
for i in range(len(df)):
    name = df.loc[i, 'item_name']
    upc_number = df.loc[i, 'upc']
    path = 'svgs/' + name.lower().replace(' ', '-')

    # Export to SVG
    my_upc = UPC(str(upc_number))
    my_upc.save(path)