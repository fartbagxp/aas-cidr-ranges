# Website can be found here: https://support.maxcdn.com/hc/en-us/articles/360036932271-IP-Blocks
# If this integration breaks, review the website for more.

import requests

class MaxCDNCidrDownloader():

  def get_range(self):
    try:
      URL = 'https://support.maxcdn.com/hc/en-us/article_attachments/360051920551/maxcdn_ips.txt'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape MaxCDN IP range endpoint, error was {e}')
      return None