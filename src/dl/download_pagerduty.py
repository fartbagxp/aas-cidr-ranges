import requests


class PagerDutyCidrDownloader():

  def __init__(self):
    self.source = 'https://app.pagerduty.com/webhook_ips'

  def get_range(self):
    try:
      r = requests.get(url=self.source)
      return r.json()
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape PagerDuty webhook IP endpoint, error was {e}')
      return None
