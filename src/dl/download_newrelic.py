import requests


class NewRelicCidrDownloader():

  def __init__(self):
    self.source = 'https://s3.amazonaws.com/nr-synthetics-assets/nat-ip-dnsname/production/ip-ranges.json'

  def get_range(self):
    try:
      r = requests.get(url=self.source)
      return r.json()
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape New Relic IP range endpoint, error was {e}')
      return None
