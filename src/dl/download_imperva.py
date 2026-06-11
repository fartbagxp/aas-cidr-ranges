import requests


class ImpervaCidrDownloader():

  def __init__(self):
    self.source = 'https://my.imperva.com/api/integration/v1/ips'

  def get_range(self):
    try:
      r = requests.get(url=self.source)
      return r.json()
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Imperva IP range endpoint, error was {e}')
      return None
