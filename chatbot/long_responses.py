import random
from os import access
import re
import requests
from requests import Session
import json
from pprint import pprint as pp

class coins:
    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token}
        self.session = Session()
        self.session.headers.update(self.headers)
    def allthecoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()
        return data
    def getprice(self, symbol):
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()
        return data
        
        
cmc = coins('52045419-00a4-40eb-915d-c9b60fb6e816')
prices = cmc.getprice("BTC")



