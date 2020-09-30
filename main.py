import pytricia
import json

from update_raw import update
from src.reader import FileReader
from src.download_zoom import ZoomCidrDownloader


def add_aws_cidr(pytrie, result):
  for prefix in result['prefixes']:
    pyt[prefix['ip_prefix']] = {
        'region': prefix['region'],
        'service': prefix['service']
    }

  for prefix in result['ipv6_prefixes']:
    pyt[prefix['ipv6_prefix']] = {
        'region': prefix['region'],
        'service': prefix['service']
    }


def add_azure_cidr(pytrie, result):
  for value in result['values']:
    for prefix in value['properties']['addressPrefixes']:
      pyt[prefix] = {
          'region': value['properties']['region'],
          'platform': value['properties']['platform'],
          'systemService': value['properties']['systemService'],
          'cloud': result['cloud']
      }


def add_gcp_cidr(pytrie, result):
  results = result.split('\n')
  for r in results:
    if r.strip():
      pyt[r] = {
          'source': 'Google',
          'website': '_cloud-netblocks.googleusercontent.com'
      }


def add_zoom_cidr(pytrie, result, source, website):
  results = result.split('\n')
  for r in results:
    if r.strip():
      pyt[r] = {
          'source': source,
          'website': website
      }


def add_cloudflare_cidr(pytrie, result):
  results = result.split('\n')
  for r in results:
    if r.strip():
      pyt[r] = {
          'source': 'Cloudflare',
          'website': 'https://www.cloudflare.com/ips/'
      }


def add_fastly_cidr(pytrie, result):
  for ipv4 in result['addresses']:
    pyt[ipv4] = {
        'source': 'Fastly',
        'website': 'https://api.fastly.com/public-ip-list'
    }
  for ipv6 in result['ipv6_addresses']:
    pyt[ipv6] = {
        'source': 'Fastly',
        'website': 'https://api.fastly.com/public-ip-list'
    }


# update()

# 128 bits needed for holding IPv6
pyt = pytricia.PyTricia(128)

reader = FileReader()
data = reader.read('data/raw/aws.json')
add_aws_cidr(pyt, json.loads(data))

data = reader.read('data/raw/azure-public.json')
add_azure_cidr(pyt, json.loads(data))

data = reader.read('data/raw/azure-china.json')
add_azure_cidr(pyt, json.loads(data))

data = reader.read('data/raw/azure-germany.json')
add_azure_cidr(pyt, json.loads(data))

data = reader.read('data/raw/azure-gov.json')
add_azure_cidr(pyt, json.loads(data))

data = reader.read('data/raw/gcp.txt')
add_gcp_cidr(pyt, data)

data = reader.read('data/raw/cloudflare-ipv4.txt')
add_cloudflare_cidr(pyt, data)

data = reader.read('data/raw/cloudflare-ipv6.txt')
add_cloudflare_cidr(pyt, data)

data = reader.read('data/raw/fastly.json')
add_fastly_cidr(pyt, json.loads(data))

zoom = ZoomCidrDownloader()
print(zoom.get_config().get('source'))
data = reader.read('data/raw/zoom-crc.txt')
add_zoom_cidr(pyt, data,
              zoom.get_config().get('source').get('zoom'),
              zoom.get_config().get('url').get('zoom'))
data = reader.read('data/raw/zoom-meeting.txt')
add_zoom_cidr(pyt, data,
              zoom.get_config().get('source').get('meeting'),
              zoom.get_config().get('url').get('meeting'))
data = reader.read('data/raw/zoom-phone.txt')
add_zoom_cidr(pyt, data,
              zoom.get_config().get('source').get('phone'),
              zoom.get_config().get('url').get('phone'))
data = reader.read('data/raw/zoom-range.txt')
add_zoom_cidr(pyt, data,
              zoom.get_config().get('source').get('range'),
              zoom.get_config().get('url').get('range'))


'''
Test it out!
'''
print(pyt.get('108.162.192.0'))
print(pyt.get('35.199.128.0'))
print(pyt.get('35.200.0.0'))
print(pyt.get('92.242.140.21'))
print(pyt.get('65.196.93.54'))
print(pyt.get('52.61.22.32'))
print(pyt.get('52.61.22.32'))
print(pyt.get('15.200.73.125'))
print(pyt.get('52.61.128.0/22'))
print(pyt.get('52.61.132.0/22'))
