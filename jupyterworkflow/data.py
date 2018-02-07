import os
from urllib.request import urlretrieve
import pandas as pd


FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename="Fremont.csv", url=FREMONT_URL, force_download=False):

    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    data.columns = ('West','East')
    data['Total'] = data['West']+data['East']
    return data