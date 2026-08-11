## Telegram publishes the CIDR ranges used by its own infrastructure.
## Documentation: https://core.telegram.org/resources/cidr.txt

import requests


class TelegramCidrDownloader():

  def __init__(self):
    self.source = 'https://core.telegram.org/resources/cidr.txt'

  def get_range(self):
    try:
      r = requests.get(url=self.source, timeout=30)
      lines = [line.strip() for line in r.text.splitlines() if line.strip()]
      ipv4 = sorted(line for line in lines if ':' not in line)
      ipv6 = sorted(line for line in lines if ':' in line)
      return {'ipv4': ipv4, 'ipv6': ipv6}
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Telegram IP range endpoint, error was {e}')
      return None
