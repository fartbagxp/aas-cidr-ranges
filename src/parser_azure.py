'''

The range of Microsoft Azure IPs are provided in a couple different locations.
Azure Public Cloud: https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519
Azure China Cloud: https://www.microsoft.com/en-us/download/details.aspx?id=57062
Azure US Government Cloud: https://www.microsoft.com/en-us/download/details.aspx?id=57063
Azure Germany Cloud: https://www.microsoft.com/en-us/download/details.aspx?id=57064

This is a parser for the set of IPs / IP ranges in CIDR notation.
'''


import requests
import datetime


class AzureCIDRParser():
  def get_timestamps(self):
    '''
    Return a list of timestamps from the past 7 days, because Azure IP tables updates once every week.
    The thought is that within 7 days, at least one link will drop for all Azure tables.
    '''
    format = '%Y%m%d'
    timestamps = [
        datetime.datetime.now().strftime(format),
        (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(format),
        (datetime.datetime.now() - datetime.timedelta(days=2)).strftime(format),
        (datetime.datetime.now() - datetime.timedelta(days=3)).strftime(format),
        (datetime.datetime.now() - datetime.timedelta(days=4)).strftime(format),
        (datetime.datetime.now() - datetime.timedelta(days=5)).strftime(format),
        (datetime.datetime.now() - datetime.timedelta(days=6)).strftime(format),
        (datetime.datetime.now() - datetime.timedelta(days=7)).strftime(format)
    ]
    return timestamps

  def get_public_range(self):
    for timestamp in self.get_timestamps():
      try:
        URL = f'https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_{timestamp}.json'
        r = requests.get(url=URL)
        if r.status_code == 200:
          data = r.json()
          print(f'Azure Timestamp was {timestamp}')
          return data
      except requests.exceptions.RequestException as e:
        print(
            f'Failure to scrape Azure Public IP range endpoint, error was {e}, timestamp was {timestamp}')
    return None

  def get_china_range(self):
    for timestamp in self.get_timestamps():
      try:
        URL = f'https://download.microsoft.com/download/9/D/0/9D03B7E2-4B80-4BF3-9B91-DA8C7D3EE9F9/ServiceTags_China_{timestamp}.json'
        r = requests.get(url=URL)
        if r.status_code == 200:
          data = r.json()
          print(f'Azure Timestamp was {timestamp}')
          return data
      except requests.exceptions.RequestException as e:
        print(
            f'Failure to scrape Azure China IP range endpoint, error was {e}, timestamp was {timestamp}')
    return None

  def get_germany_range(self):
    for timestamp in self.get_timestamps():
      try:
        URL = f'https://download.microsoft.com/download/0/7/6/076274AB-4B0B-4246-A422-4BAF1E03F974/ServiceTags_AzureGermany_{timestamp}.json'
        r = requests.get(url=URL)
        if r.status_code == 200:
          data = r.json()
          print(f'Azure Timestamp was {timestamp}')
          return data
      except requests.exceptions.RequestException as e:
        print(
            f'Failure to scrape Azure Germany IP range endpoint, error was {e}, timestamp was {timestamp}')
    return None

  def get_gov_range(self):

    for timestamp in self.get_timestamps():
      try:
        URL = f'https://download.microsoft.com/download/6/4/D/64DB03BF-895B-4173-A8B1-BA4AD5D4DF22/ServiceTags_AzureGovernment_{timestamp}.json'
        r = requests.get(url=URL)
        if r.status_code == 200:
          data = r.json()
          print(f'Azure Timestamp was {timestamp}')
          return data
      except requests.exceptions.RequestException as e:
        print(
            f'Failure to scrape Azure Gov IP range endpoint, error was {e}, timestamp was {timestamp}')
    return None
