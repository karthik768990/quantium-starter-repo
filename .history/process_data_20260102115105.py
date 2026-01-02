import pandas as pd 
from pathlib import Path 

data_path = Path("data")

csv_files = list(data_path.glob('*.csv'))


processed_files = []

for file in csv_files:
        df = pd.read_csv(file)

        df = df[df['product']=="Pink Morsels"]

        df['Sales'] = df['quantity']*df['price']


        df = df['Sales', 'date','region']


        df = df.rename(columns ={
                'date' : "Date",
                'region' : "Region"
        })


        processed_files.append(df)


final_df = pd.concat(processed_files,ignore_index=True)


final_df.to_csv("pink_morsels_sales.csv",index =False)
