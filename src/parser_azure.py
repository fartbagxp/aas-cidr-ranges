'''

Azure Public Cloud: https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519
Azure China Cloud: https://www.microsoft.com/en-us/download/details.aspx?id=57062
Azure US Government Cloud: https://www.microsoft.com/en-us/download/details.aspx?id=57063
Azure Germany Cloud: https://www.microsoft.com/en-us/download/details.aspx?id=57064
'''


import requests


class AzureCIDRParser():
  def get_public_range(self):
    try:
      URL = 'https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20200323.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Azure Public IP range endpoint, error was {e}')
      return None

  def get_china_range(self):
    try:
      URL = 'https://download.microsoft.com/download/9/D/0/9D03B7E2-4B80-4BF3-9B91-DA8C7D3EE9F9/ServiceTags_China_20200323.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Azure China IP range endpoint, error was {e}')
      return None

  def get_germany_range(self):
    try:
      URL = 'https://download.microsoft.com/download/0/7/6/076274AB-4B0B-4246-A422-4BAF1E03F974/ServiceTags_AzureGermany_20200323.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(
          f'Failure to scrape Azure Germany IP range endpoint, error was {e}')
      return None

  def get_gov_range(self):
    try:
      URL = 'https://download.microsoft.com/download/6/4/D/64DB03BF-895B-4173-A8B1-BA4AD5D4DF22/ServiceTags_AzureGovernment_20200323.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(
          f'Failure to scrape Azure Gov IP range endpoint, error was {e}')
      return None
