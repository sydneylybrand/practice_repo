"""
Author: Sydney Lybrand
Date started: May 18, 2024
Purpose: To read in a JSON file and parse out the data.  Can be all of the data or can extract certain ones, like by names which start with a certain character or string, for example.
"""

import pandas as pd
import json
from flatten_json import flatten

with open('json_file_name.json') as f:
    data = json.load(f)

new_data = flatten(data)

df = pd.DataFrame.from_dict(new_data, orient = 'index')
df = df.reset_index()

df = df[0]
#df = df[df.str.startswith('ghcndaily')]
print(df)
#df.to_csv('new_csv_file_name.csv')
