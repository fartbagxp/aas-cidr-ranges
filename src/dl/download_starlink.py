import requests


class StarlinkCidrDownloader():

  def __init__(self):
    self.source = 'https://geoip.starlinkisp.net/feed.csv'

  def get_range(self):
    try:
      r = requests.get(url=self.source)
      return r.text
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Starlink geofeed, error was {e}')
      return None
