import requests


class VultrCidrDownloader():

  def __init__(self):
    self.source = 'https://geofeed.constant.com/?json'

  def get_range(self):
    try:
      r = requests.get(url=self.source)
      return r.json()
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Vultr geofeed, error was {e}')
      return None
