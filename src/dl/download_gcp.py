# To pull the google cloud environment IPs, we should pull from the google source.
# Documentation: https://cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults.

import requests

class GcpCidrDownloader():

  def get_range(self):
    try:
      URL = 'https://www.gstatic.com/ipranges/cloud.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Google Cloud IP range endpoint, error was {e}')
      return None
