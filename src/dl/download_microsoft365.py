## Data is pulled from the Microsoft 365 IP Address and URL web service.
## Documentation: https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-ip-web-service
##
## The service requires a client-generated GUID as the clientrequestid parameter.
## The Germany instance was retired alongside Microsoft Cloud Deutschland in 2021.

import uuid

import requests

class Microsoft365CidrDownloader():

  def get_config(self):
    config = [
      {
        "for": "Microsoft 365 Worldwide (including GCC)",
        "instance": "Worldwide",
        "link": "https://endpoints.office.com/endpoints/worldwide",
        "name": "m365-worldwide.json"
      },
      {
        "for": "Microsoft 365 U.S. Government GCC High",
        "instance": "USGovGCCHigh",
        "link": "https://endpoints.office.com/endpoints/USGovGCCHigh",
        "name": "m365-usgov-gcchigh.json"
      },
      {
        "for": "Microsoft 365 U.S. Government DoD",
        "instance": "USGovDoD",
        "link": "https://endpoints.office.com/endpoints/USGovDoD",
        "name": "m365-usgov-dod.json"
      },
      {
        "for": "Microsoft 365 operated by 21Vianet (China)",
        "instance": "China",
        "link": "https://endpoints.office.com/endpoints/China",
        "name": "m365-china.json"
      }
    ]
    return config

  def get_range(self, info):
    try:
      params = {'clientrequestid': str(uuid.uuid4())}
      r = requests.get(url=info['link'], params=params)
      endpoints = r.json()
      data = {
        'for': info['for'],
        'instance': info['instance'],
        'link': info['link'],
        'endpoints': endpoints
      }
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Microsoft 365 IP range endpoint, error was {e}')
      return None
