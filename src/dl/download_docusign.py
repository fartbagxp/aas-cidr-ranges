import re
import requests

_IPV4_CIDR = re.compile(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})\b')


class DocuSignCidrDownloader():

  def __init__(self):
    self.source = 'https://www.docusign.com/trust/security/esignature'

  def get_range(self):
    try:
      r = requests.get(url=self.source, timeout=30)
      cidrs = sorted(set(_IPV4_CIDR.findall(r.text)))
      return {'ipv4': cidrs}
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape DocuSign IP range page, error was {e}')
      return None
