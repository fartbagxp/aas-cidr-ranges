# Information about Github.com public IPs can be found here:
# https://help.github.com/en/github/authenticating-to-github/about-githubs-ip-addresses

# Endpoint for IP address - https://api.github.com/meta

import requests


class GithubCidrDownloader():

  def get_range(self):
    try:
      URL = 'https://api.github.com/meta'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Github IP range endpoint, error was {e}')
      return None
