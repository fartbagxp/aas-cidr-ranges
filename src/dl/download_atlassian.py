'''
The range of Atlassian services IPs are provided in this location:
Atlassian includes a suite of cloud services such as Statuspage, Jira, Confluence, etc.

This is a parser for the set of IPs / IP ranges in CIDR notation.
'''

import requests


class AtlassianCidrDownloader():
  def get_range(self):
    try:
      URL = 'https://ip-ranges.atlassian.com/'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Atlassian IP range endpoint, error was {e}')
      return None
