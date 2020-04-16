'''

The range of Cloudflare IPs are provided in this location:
https://www.cloudflare.com/ips/

This is a parser for the set of IPs / IP ranges in CIDR notation.
'''

import requests


class CloudflareCIDRParser():
  def get_range_v4(self):
    try:
      URL = 'https://www.cloudflare.com/ips-v4'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Cloudflare IPv4 range endpoint, error was {e}')
      return None

  def get_range_v6(self):
    try:
      URL = 'https://www.cloudflare.com/ips-v6'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Cloudflare IPv6 range endpoint, error was {e}')
      return None
