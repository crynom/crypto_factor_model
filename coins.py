import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import datetime as date
from scipy.stats import kurtosis, skew

class Coin:

    def __init__(self, pair, interval = 60, since = None):
        self.since = since
        self.pair = pair.upper()
        self.interval = interval
        self.tdata, self.data = self.get_quote()
        self.stats()

    def __repr__(self):
        return str(self.pair)

    def get_quote(self):
        if self.since == None:
            resp = requests.get(f'https://api.kraken.com/0/public/OHLC?pair={self.pair}&interval={self.interval}')
        else:
            resp = requests.get(f'https://api.kraken.com/0/public/OHLC?pair={self.pair}&interval={self.interval}&since{self.since}')
        data = resp.json()
        for val in data['result'][self.pair]:
            # val[0] = date.datetime.fromtimestamp(val[0])
            for i in range(1,7):
                val[i] = float(val[i])
        df = pd.DataFrame.from_dict(data['result'][self.pair])
        df = df.set_axis(['time','open','high','low','close','vwap','volume','count'], axis='columns').reset_index(drop=True)
        dt = pd.DataFrame.from_dict(data['result'][self.pair])
        dt = dt.set_axis(['time','open','high','low','close','vwap','volume','count'], axis='columns').reset_index(drop=True)
        for time in dt.loc[:,'time']:
            dt.time = date.datetime.fromtimestamp(time)
        return df, dt

    def stats(self, verbose=0):
        self.logrs = np.log(self.data.close/self.data.close.shift(1)).dropna()
        self.logm = np.mean(self.logrs)
        self.logr = sum(self.logrs)
        self.var = np.var(self.logrs)
        self.std = np.std(self.logrs)
        self.skew = skew(self.logrs)
        self.kurt = kurtosis(self.logrs)
        if verbose == 1:
            print(f'Return: {self.logr:.2%}')

    
    

if __name__ == '__main__':
    pass