## Documentation: https://help.salesforce.com/s/articleView?id=000384438&type=1
## Salesforce publishes the full set of its IP ranges as a single JSON document.

import requests

class SalesforceCidrDownloader():

  def get_range(self):
    try:
      URL = 'https://ip-ranges.salesforce.com/ip-ranges.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Salesforce IP range endpoint, error was {e}')
      return None
