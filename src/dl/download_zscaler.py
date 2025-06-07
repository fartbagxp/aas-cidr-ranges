## Data is pulled from https://config.zscaler.com/

import requests

class ZScalerCidrDownloader():

  def get_config(self):
    config = [
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscaler.net",
        "section": "Cloud Enforcement Node Ranges",
        "link": "https://api.config.zscaler.com/zscaler.net/cenr/json",
        "name": "zscaler.net-cenr.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscaler.net",
        "section": "Zscaler Hub IP addresses",
        "link": "https://api.config.zscaler.com/zscaler.net/hubs/cidr/json/recommended",
        "name": "zscaler.net-hub.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalerone.net",
        "section": "Cloud Enforcement Node Ranges",
        "link": "https://api.config.zscaler.com/zscalerone.net/cenr/json",
        "name": "zscalerone.net-cenr.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalerone.net",
        "section": "Zscaler Hub IP addresses",
        "link": "https://api.config.zscaler.com/zscalerone.net/hubs/cidr/json/recommended",
        "name": "zscalerone.net-hub.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalertwo.net",
        "section": "Cloud Enforcement Node Ranges",
        "link": "https://api.config.zscaler.com/zscalertwo.net/cenr/json",
        "name": "zscalertwo.net-cenr.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalertwo.net",
        "section": "Zscaler Hub IP addresses",
        "link": "https://api.config.zscaler.com/zscalertwo.net/hubs/cidr/json/recommended",
        "name": "zscalertwo.net-hub.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalerthree.net",
        "section": "Cloud Enforcement Node Ranges",
        "link": "https://api.config.zscaler.com/zscalerthree.net/cenr/json",
        "name": "zscalerthree.net-cenr.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalerthree.net",
        "section": "Zscaler Hub IP addresses",
        "link": "https://api.config.zscaler.com/zscalerthree.net/hubs/cidr/json/recommended",
        "name": "zscalerthree.net-hub.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscloud.net",
        "section": "Cloud Enforcement Node Ranges",
        "link": "https://api.config.zscaler.com/zscloud.net/cenr/json",
        "name": "zscloud.net-cenr.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscloud.net",
        "section": "Zscaler Hub IP addresses",
        "link": "https://api.config.zscaler.com/zscloud.net/hubs/cidr/json/recommended",
        "name": "zscloud.net-hub.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalerbeta.net",
        "section": "Cloud Enforcement Node Ranges",
        "link": "https://api.config.zscaler.com/zscalerbeta.net/cenr/json",
        "name": "zscalerbeta.net-cenr.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalerbeta.net",
        "section": "Zscaler Hub IP addresses",
        "link": "https://api.config.zscaler.com/zscalerbeta.net/hubs/cidr/json/recommended",
        "name": "zscalerbeta.net-hub.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalergov.net",
        "section": "Cloud Enforcement Node Ranges",
        "link": "https://api.config.zscaler.com/zscalergov.net/cenr/json",
        "name": "zscalergov.net-cenr.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalergov.net",
        "section": "Zscaler Hub IP addresses",
        "link": "https://api.config.zscaler.com/zscalergov.net/hubs/cidr/json/recommended",
        "name": "zscalergov.net-hub.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalerten.net",
        "section": "Cloud Enforcement Node Ranges",
        "link": "https://api.config.zscaler.com/zscalerten.net/cenr/json",
        "name": "zscalerten.net-cenr.json"
      },
      {
        "for": "ZScaler Internet Access (ZIA)",
        "cloud": "zscalerten.net",
        "section": "Zscaler Hub IP addresses",
        "link": "https://api.config.zscaler.com/zscalerten.net/hubs/cidr/json/recommended",
        "name": "zscalerten.net-hub.json"
      },
      {
        "for": "Zscaler Digital Exchange (ZDX)",
        "cloud": "zdxcloud.net",
        "section": "Zscaler Hub IP addresses",
        "link": "https://api.config.zscaler.com/zdxcloud.net/hubs/cidr/json/recommended",
        "name": "zdxcloud.net-hub.json"
      },
      {
        "for": "Zscaler Digital Exchange (ZDX)",
        "cloud": "zdxgov.net",
        "section": "Zscaler Hub IP addresses",
        "link": "https://api.config.zscaler.com/zdxgov.net/hubs/cidr/json/recommended",
        "name": "zdxgov.net-hub.json"
      },
      {
        "for": "Zscaler Digital Exchange (ZDX)",
        "cloud": "zdxbeta.net",
        "section": "Zscaler Hub IP addresses",
        "link": "https://api.config.zscaler.com/zdxbeta.net/hubs/cidr/json/recommended",
        "name": "zdxbeta.net-hub.json"
      }
    ]
    return config

  def get_range(self, info):
    try:
      r = requests.get(url=info['link'])
      data = r.json()
      data['for'] = info['for']
      data['cloud'] = info['cloud']
      data['section'] = info['section']
      data['link'] = info['link']
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape ZScaler IP range endpoint, error was {e}')
      return None
