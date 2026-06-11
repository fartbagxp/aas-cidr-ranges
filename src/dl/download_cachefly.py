import requests


class CacheFlyCidrDownloader():

  def __init__(self):
    self.source = 'https://cachefly.cachefly.net/ips/cdn.txt'

  def get_range(self):
    try:
      r = requests.get(url=self.source)
      return r.text
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape CacheFly CDN IP list, error was {e}')
      return None
