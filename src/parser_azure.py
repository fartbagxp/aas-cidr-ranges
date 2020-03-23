'''

Azure Public Cloud: https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519
Azure GovCloud: https://www.microsoft.com/en-us/download/details.aspx?id=57063
'''


import requests


class AzureCIDRParser():
  def get_range(self):
    try:
      URL = 'https://download.microsoft.com/download/7/1/D/71D86715-5596-4529-9B13-DA13A5DE5B63/ServiceTags_Public_20200316.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape AWS IP range endpoint, error was {e}')
      return None

  def get_gov_range(self):
    try:
      URL = 'https://download.microsoft.com/download/6/4/D/64DB03BF-895B-4173-A8B1-BA4AD5D4DF22/ServiceTags_AzureGovernment_20200316.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape AWS IP range endpoint, error was {e}')
      return None
