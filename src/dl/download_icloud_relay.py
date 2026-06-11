import requests


class ICloudRelayCidrDownloader():

  def __init__(self):
    self.source = 'https://mask-api.icloud.com/egress-ip-ranges.csv'

  def get_range(self):
    try:
      r = requests.get(url=self.source)
      return r.text
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Apple iCloud Private Relay egress IP ranges, error was {e}')
      return None
