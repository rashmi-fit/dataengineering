"""
This is a python extract transform and load example to create ETL pipeline
"""

import requests
import pandas as pd
from sqlalchemy import create_engine

# Extract data from API

def extract()-> dict:
      API_url = "http://universities.hipolabs.com/search?country=United+States"
      # API_url = "https://api.covid19india.org/data.json"
      data = requests.get(API_url).json()
      return data

def transform(data:dict)->pd.DataFrame:
      df = pd.DataFrame(data)
      print(f'total number of universities: {len(data)}')
      df = df[df.name.str.contains("California")]
      print(f'number of universities in california {len(df)}')
      df.domains = [ ','.join(map(str,l)) for l in df.domains]
      df['web_pages'] = [','.join(map(str, l)) for l in df['web_pages']]
      df = df.reset_index(drop=True)
      return df[["domains","country","web_pages","name"]]

"""Load the data a sqllite database"""
def load(df:pd.DataFrame)->None:
      db_connection_string="sqlite:///my_lite_store.db"
      disk_engine = create_engine(db_connection_string)
      df.to_sql('cal_uni', disk_engine, if_exists='replace')

data =extract()
df = transform(data)
# you have to set up below and then its going to work
# load(df)
