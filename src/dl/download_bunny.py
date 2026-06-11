import requests


class BunnyCidrDownloader():

  def get_range_v4(self):
    try:
      r = requests.get(url='https://api.bunny.net/system/edgeserverlist')
      return r.json()
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Bunny.net IPv4 edge server list, error was {e}')
      return None

  def get_range_v6(self):
    try:
      r = requests.get(url='https://api.bunny.net/system/edgeserverlist/ipv6')
      return r.json()
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Bunny.net IPv6 edge server list, error was {e}')
      return None
