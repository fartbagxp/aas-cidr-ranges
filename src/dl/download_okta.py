## Documentation: https://help.okta.com/en/prod/Content/Topics/Security/ip-address-allow-listing.htm

import requests

class OktaCidrDownloader():

  def get_range(self):
    try:
      URL = 'https://s3.amazonaws.com/okta-ip-ranges/ip_ranges.json'
      r = requests.get(url=URL)
      data = r.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Okta IP range endpoint, error was {e}')
      return None
