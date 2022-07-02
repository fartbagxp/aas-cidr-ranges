import requests

class OracleCidrDownloader():

  def get_range(self):
    try:
      URL = 'https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Oracle IP range endpoint, error was {e}')
      return None