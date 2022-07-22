'''
IANA is the Internet Assigned Numbers Authority, an organization which governs 
IP address allocation. We use IANA as the official source of truth for private 
IP address range allocation.

Private IP ranges typically include only IP addresses (ex. 10.0.0.1, 127.0.0.1) 
that are only active within a local area network (LAN).

The source for private IP address blocks can be found here:
IPv4: https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
IPv6: https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml

There's a link to download a comma separated file .csv for each of the 
respective IP address blocks.
'''

import requests

class IanaCidrDownloader():

  def get_ipv4_block(self):
    try:
      URL = 'https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry-1.csv'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape IANA IP range endpoint, error was {e}')
      return None

  def get_ipv6_block(self):
    try:
      URL = 'https://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry-1.csv'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape IANA IP range endpoint, error was {e}')
      return None