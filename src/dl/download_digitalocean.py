# Documentation can be found here: https://www.digitalocean.com/docs/platform/

import requests

class DigitalOceanCidrDownloader():

  def get_range(self):
    try:
      URL = 'https://digitalocean.com/geo/google.csv'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Digital Ocean IP range endpoint, error was {e}')
      return None
