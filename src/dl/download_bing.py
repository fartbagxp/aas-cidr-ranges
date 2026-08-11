## Documentation: https://www.bing.com/webmasters/help/verify-bingbot-2195837f

import requests


class BingCidrDownloader():

  def __init__(self):
    self.source = 'https://www.bing.com/toolbox/bingbot.json'

  def get_range(self):
    try:
      r = requests.get(url=self.source, timeout=30)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Bingbot IP range endpoint, error was {e}')
      return None
