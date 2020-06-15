# Endpoint: https://api.fastly.com/public-ip-list


import requests

class FastlyCIDRParser():

  def get_range(self):
    try:
      URL = 'https://api.fastly.com/public-ip-list'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Fastly IP range endpoint, error was {e}')
      return None