## Generic ASN-based downloader for providers that do not publish an official
## machine-readable IP range file (most Chinese and European cloud providers).
##
## Announced prefixes are pulled from the RIPEstat Data API:
## https://stat.ripe.net/docs/02.data-api/announced-prefixes.html
##
## Note that BGP announcements describe everything a provider announces, not
## just customer-facing service ranges, so there is no service/region tagging
## like the official feeds provide.
##
## Alternative sources for cross-checking: bgp.tools, RADb whois, e.g.
## whois -h whois.radb.net -- '-i origin AS16276' | grep -Eo "([0-9.]+){4}/[0-9]+"

import requests

class AsnCidrDownloader():

  def get_config(self):
    config = [
      {
        "for": "Alibaba Cloud (international)",
        "asn": "AS45102",
        "name": "asn-alibaba-as45102.json"
      },
      {
        "for": "Alibaba Cloud (China)",
        "asn": "AS37963",
        "name": "asn-alibaba-as37963.json"
      },
      {
        "for": "Tencent Cloud (international)",
        "asn": "AS132203",
        "name": "asn-tencent-as132203.json"
      },
      {
        "for": "Tencent Cloud (China)",
        "asn": "AS45090",
        "name": "asn-tencent-as45090.json"
      },
      {
        "for": "Huawei Cloud",
        "asn": "AS136907",
        "name": "asn-huawei-as136907.json"
      },
      {
        "for": "Baidu Cloud",
        "asn": "AS38365",
        "name": "asn-baidu-as38365.json"
      },
      {
        "for": "OVHcloud",
        "asn": "AS16276",
        "name": "asn-ovh-as16276.json"
      },
      {
        "for": "OVHcloud (US)",
        "asn": "AS35540",
        "name": "asn-ovh-as35540.json"
      },
      {
        "for": "Hetzner",
        "asn": "AS24940",
        "name": "asn-hetzner-as24940.json"
      },
      {
        "for": "Scaleway",
        "asn": "AS12876",
        "name": "asn-scaleway-as12876.json"
      },
      {
        "for": "IONOS",
        "asn": "AS8560",
        "name": "asn-ionos-as8560.json"
      }
    ]
    return config

  def get_range(self, info):
    try:
      URL = 'https://stat.ripe.net/data/announced-prefixes/data.json'
      params = {'resource': info['asn'], 'sourceapp': 'aas-cidr-ranges'}
      r = requests.get(url=URL, params=params)
      data = r.json()
      data['for'] = info['for']
      data['asn'] = info['asn']
      return data
    except requests.exceptions.RequestException as e:
      print(f"Failure to scrape RIPEstat announced prefixes for {info['asn']}, error was {e}")
      return None
