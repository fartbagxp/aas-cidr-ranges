'''
The range of Pingdom probes from various locations.
The documentation can be found here:
https://documentation.solarwinds.com/en/success_center/pingdom/content/topics/pingdom-probe-servers-ip-addresses.htm?cshid=pd-rd_203682601-pingdom-probe-servers-ip-addresses

This is a parser for the set of IPs / IP ranges in CIDR notation.
'''

import requests


class PingdomCidrDownloader():

  def get_range_v4(self):
    try:
      URL = 'https://my.pingdom.com/probes/ipv4'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Pingdom IPv4 range endpoint, error was {e}')
      return None

  def get_range_v6(self):
    try:
      URL = 'https://my.pingdom.com/probes/ipv6'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Pingdom IPv6 range endpoint, error was {e}')
      return None
