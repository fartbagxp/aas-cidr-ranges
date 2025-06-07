'''
The range of Datadog HQ
https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html

This is a parser for the set of IPs / IP ranges in CIDR notation.
'''

import requests

class DatadogCidrDownloader():

  def __init__(self):
    self.source = 'https://ip-ranges.datadoghq.com/'

  def get_range(self):
    try:
      URL = self.source
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Datadog IP range endpoint, error was {e}')
      return None


def get_source(self):
  return self.source
