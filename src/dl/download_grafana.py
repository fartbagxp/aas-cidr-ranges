# Documentation can be found here: https://grafana.com/docs/grafana-cloud/reference/allow-list/

import requests
from ..async_dns import resolve_all_dns

class GrafanaCidrDownloader():

  def get_hosted_alerts_range(self):
    try:
      URL = 'https://grafana.com/api/hosted-alerts/source-ips.txt'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Grafana IP range endpoint, error was {e}')
      return None

  def get_hosted_grafana_range(self):
    try:
      URL = 'https://grafana.com/api/hosted-grafana/source-ips.txt'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Grafana IP range endpoint, error was {e}')
      return None

  def get_hosted_metrics_range(self):
    try:
      URL = 'https://grafana.com/api/hosted-metrics/source-ips.txt'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Grafana IP range endpoint, error was {e}')
      return None

  def get_hosted_traces_range(self):
    try:
      URL = 'https://grafana.com/api/hosted-traces/source-ips.txt'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Grafana IP range endpoint, error was {e}')
      return None

  def get_hosted_logs_range(self):
    try:
      URL = 'https://grafana.com/api/hosted-logs/source-ips.txt'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Grafana IP range endpoint, error was {e}')
      return None

  def get_dns_names(self):
    # This list came from https://grafana.com/docs/grafana-cloud/reference/allow-list/
    dns_list = [
      'sm-amsterdam.grafana.net',
      'sm-atlanta.grafana.net'
      'sm-bangalore.grafana.net',
      'sm-capetown.grafana.net',
      'sm-dallas.grafana.net',
      'sm-frankfurt.grafana.net',
      'sm-london.grafana.net',
      'sm-mumbai.grafana.net',
      'sm-newark.grafana.net',
      'sm-newyork.grafana.net',
      'sm-northcalifornia.grafana.net',
      'sm-northvirginia.grafana.net',
      'sm-ohio.grafana.net',
      'sm-oregon.grafana.net',
      'sm-paris.grafana.net',
      'sm-sanfrancisco.grafana.net',
      'sm-saopaulo.grafana.net',
      'sm-seoul.grafana.net',
      'sm-singapore.grafana.net',
      'sm-sydney.grafana.net',
      'sm-tokyo.grafana.net',
      'sm-toronto.grafana.net',
    ]
    results = resolve_all_dns(dns_list)
    return results
