import requests


class MongoDBAtlasCidrDownloader():

  def __init__(self):
    self.source = 'https://cloud.mongodb.com/api/atlas/v2/unauth/controlPlaneIPAddresses'

  def get_range(self):
    try:
      r = requests.get(
        url=self.source,
        headers={'Accept': 'application/vnd.atlas.2023-11-15+json'},
      )
      return r.json()
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape MongoDB Atlas IP range endpoint, error was {e}')
      return None
