import pandas as pd 
from pathlib import Path 

data_path = Path("data")

csv_files = list(data_path.glob('*.csv'))


processed_files = []

for file in csv_files:
        