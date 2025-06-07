# This pulls the list of google based services outside of google cloud.
# Documentation: https://support.google.com/a/answer/60764

import requests

class GcpCidrDownloader():

  def get_range(self):
    try:
      URL = 'https://www.gstatic.com/ipranges/goog.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Google Cloud IP range endpoint, error was {e}')
      return None
