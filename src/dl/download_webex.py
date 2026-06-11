import re
import requests

_IPV4_CIDR = re.compile(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})\b')
# matches compressed IPv6 CIDR like 2607:fcf0::/32 or 2402:2500:1000::/36
_IPV6_CIDR = re.compile(r'\b([0-9a-fA-F]{1,4}(?::[0-9a-fA-F]{0,4})+::/\d{1,3})\b')


class WebexCidrDownloader():

  def __init__(self):
    self.source = 'https://help.webex.com/en-us/article/WBX264/'

  def get_range(self):
    try:
      r = requests.get(url=self.source, timeout=30)
      ipv4 = sorted(set(_IPV4_CIDR.findall(r.text)))
      ipv6 = sorted(set(_IPV6_CIDR.findall(r.text)))
      return {'ipv4': ipv4, 'ipv6': ipv6}
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Cisco Webex IP range page, error was {e}')
      return None
