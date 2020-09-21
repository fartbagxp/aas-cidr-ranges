import pytricia

from src.download_aws import AWSCidrDownloader
from src.download_azure import AzureCidrDownloader
from src.download_zoom import ZoomCidrDownloader
from src.download_cloudflare import CloudflareCidrDownloader
from src.download_fastly import FastlyCidrDownloader
from src.download import CidrWriter


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
  for value in result['data']:
    pyt[value] = {
        'source': result['source'],
        'last_updated': result['last_updated']
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


# 128 bits needed for holding IPv6
pyt = pytricia.PyTricia(128)

aws_parser = AWSCidrDownloader()
result = aws_parser.get_range()
add_aws_cidr(pyt, result)

'''
Testing - AWS
{'region': 'us-east-1', 'service': 'EC2'}
{'region': 'eu-west-2', 'service': 'S3'}
'''
print(pyt.get('52.95.245.0'))
print(pyt.get('2a05:d07a:c000::'))

print(pyt.get('18.253.194.205'))

azure_parser = AzureCidrDownloader()
result = azure_parser.get_public_range()
add_azure_cidr(pyt, result)

result = azure_parser.get_china_range()
add_azure_cidr(pyt, result)

result = azure_parser.get_germany_range()
add_azure_cidr(pyt, result)

result = azure_parser.get_gov_range()
add_azure_cidr(pyt, result)

'''
Testing - Azure
{'region': '', 'platform': 'Azure', 'systemService': '', 'cloud': 'Public'}
{'region': '', 'platform': 'Azure',
    'systemService': 'AzureAppConfiguration', 'cloud': 'AzureGovernment'}
'''
print(pyt.get('213.199.183.0'))
print(pyt.get('52.127.61.112'))

# gcp_parser = GoogleCidrDownloader()
# result = gcp_parser.get_range()
# add_gcp_cidr(pyt, result)

# '''
# Testing - Google

# '''
# print(pyt.get('35.199.128.0'))
# print(pyt.get('35.200.0.0'))


cloudflare_parser = CloudflareCidrDownloader()
result = cloudflare_parser.get_range_v4()
add_cloudflare_cidr(pyt, result)

result = cloudflare_parser.get_range_v6()
add_cloudflare_cidr(pyt, result)

'''
Testing - Cloudflare
'''
print(pyt.get('108.162.192.0'))
print(pyt.get('2c0f:f248::'))

fastly_parser = FastlyCidrDownloader()
result = fastly_parser.get_range()
pyt = pytricia.PyTricia()
add_fastly_cidr(pyt, result)

'''
Testing - Fastly
'''
print(pyt.get('23.235.32.0'))
print(pyt.get('2a04:4e40::'))
print(pyt.get('2c0f:f248::'))

zoom_parser = ZoomCidrDownloader()
result, source, website = zoom_parser.get_zoom_range()
add_zoom_cidr(pyt, result, source, website)
result, source, website = zoom_parser.get_zoom_meeting_range()
add_zoom_cidr(pyt, result, source, website)
result, source, website = zoom_parser.get_zoom_crc_range()
add_zoom_cidr(pyt, result, source, website)
result, source, website = zoom_parser.get_zoom_phone_range()
add_zoom_cidr(pyt, result, source, website)

'''
Testing - Zoom
'''

print(pyt.get('3.80.20.128'))
print(pyt.get('103.122.166.0'))
