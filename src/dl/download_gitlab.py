import re
import requests

_IPV4_CIDR = re.compile(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})\b')
# individual IPs not in a CIDR block
_IPV4_HOST = re.compile(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b')


class GitLabCidrDownloader():

  def __init__(self):
    self.source = 'https://docs.gitlab.com/ee/user/gitlab_com/#ip-range'

  def get_range(self):
    try:
      r = requests.get(url=self.source, timeout=30)
      text = r.text
      cidrs = sorted(set(_IPV4_CIDR.findall(text)))
      # collect host IPs that aren't already covered by a CIDR
      all_ips = set(_IPV4_HOST.findall(text))
      cidr_ips = set(_IPV4_CIDR.findall(text))
      hosts = sorted(all_ips - cidr_ips)
      return {'ipv4_cidrs': cidrs, 'ipv4_hosts': hosts}
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape GitLab.com IP range page, error was {e}')
      return None
