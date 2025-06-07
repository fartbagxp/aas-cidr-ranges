import requests

class SeqeraCidrDownloader():

  def get_range(self):
    try:
      URL = 'https://meta.seqera.io/'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Seqera IP range endpoint, error was {e}')
      return None