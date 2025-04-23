import pandas as pd
import barcode

df = pd.read_csv('database/database.csv')

UPC = barcode.get_barcode_class('upc')

for index, row in df.iterrows():
    upc_number = str(row.UPC)
    name = 'svgs/' + row['Item Name'].lower().replace(' ','-')
    my_upc = UPC(upc_number)
    my_upc.save(name)