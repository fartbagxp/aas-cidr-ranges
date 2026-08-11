## StatusCake publishes the IP addresses of its uptime monitoring nodes directly.
## Documentation: https://www.statuscake.com/kb/knowledge-base/what-are-your-ip-addresses/

import requests


class StatusCakeCidrDownloader():

  def __init__(self):
    self.source = 'https://app.statuscake.com/Workfloor/Locations.php?format=txt'

  def get_range(self):
    try:
      r = requests.get(url=self.source, timeout=30)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape StatusCake IP range endpoint, error was {e}')
      return None
