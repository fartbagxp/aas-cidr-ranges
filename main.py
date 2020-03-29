import pytricia
from pprint import pprint
from src.parser_aws import AWSCIDRParser
from src.parser_azure import AzureCIDRParser
from src.parser_gcp import GoogleCIDRParser
from src.parser_zoom import ZoomCIDRParser


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


def add_zoom_cidr(pytrie, result):
  for values in result['data']:
    for value in values['Destination']:
      try:
        pyt[value] = {
            'source': result['source'],
            'last_updated': result['last_updated'],
            'connectionType': values['ConnectionType'],
            'protocol': values['Protocol'],
            'ports': values['Ports'],
            'sourceName': values['SourceName']
        }
      except:
        '''
        Best effort scraping the data for IP CIDR ranges
        '''
        pass


aws_parser = AWSCIDRParser()
result = aws_parser.get_range()
pyt = pytricia.PyTricia()
add_aws_cidr(pyt, result)

'''
Testing - AWS
{'region': 'us-east-1', 'service': 'EC2'}
{'region': 'me-south-1', 'service': 'AMAZON'}
'''
print(pyt.get('52.95.245.0'))
print(pyt.get('2a05:d07e:e000::'))

azure_parser = AzureCIDRParser()
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

gcp_parser = GoogleCIDRParser()
result = gcp_parser.get_range()
add_gcp_cidr(pyt, result)

'''
Testing - Google

'''
print(pyt.get('35.199.128.0'))
print(pyt.get('35.200.0.0'))

zoom_parser = ZoomCIDRParser()
result = zoom_parser.get_range()
add_zoom_cidr(pyt, result)

'''
Testing - Zoom

'''
print(pyt.get('3.80.20.128'))
print(pyt.get('103.122.166.0'))
