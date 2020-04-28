__version__ = '0.1.0'

import datetime
import urllib.request
from io import BytesIO

import pandas as pd


def get_rawdata():
    url = 'https://covidtracking.com/api/v1/states/daily.csv'
    response = urllib.request.urlopen(url)
    return response.read()  # a `bytes` object


def get_state_by_abbr():
    return 1


def parsedate(s: str):
    return datetime.datetime.strptime(s, '%Y%m%d')


def getdata():
    raw = get_rawdata()
    df = pd.read_csv(BytesIO(raw), encoding='utf8', dtype={'date': str, 'state': str})
    return df
