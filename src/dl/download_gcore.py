import requests


class GcoreCidrDownloader():

  def __init__(self):
    self.source = 'https://api.gcore.com/cdn/public-ip-list'

  def get_range(self):
    try:
      r = requests.get(url=self.source)
      return r.json()
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Gcore CDN IP list, error was {e}')
      return None
