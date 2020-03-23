'''
The range of Amazon Web Service (AWS) IPs are provided in this location:
https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html

This is a parser for the set of IPs / IP ranges in CIDR notation.
'''

import requests


class AWSCIDRParser():
  def get_range(self):
    try:
      URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape AWS IP range endpoint, error was {e}')
      return None
