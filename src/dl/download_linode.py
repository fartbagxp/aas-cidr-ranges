import requests

class LinodeCidrDownloader():

  def get_range(self):
    try:
      URL = 'https://geoip.linode.com/'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Linode IP range endpoint, error was {e}')
      return None