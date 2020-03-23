import pytricia
from pprint import pprint
from src.parser_aws import AWSCIDRParser
from src.parser_azure import AzureCIDRParser

aws_parser = AWSCIDRParser()
result = aws_parser.get_range()

pyt = pytricia.PyTricia()
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

'''
Testing - AWS
{'region': 'us-east-1', 'service': 'EC2'}
{'region': 'me-south-1', 'service': 'AMAZON'}
'''
# print(pyt.get('52.95.245.0'))
# print(pyt.get('2a05:d07e:e000::'))

azure_parser = AzureCIDRParser()
result = azure_parser.get_range()
for value in result['values']:
  for prefix in value['properties']['addressPrefixes']:
    pyt[prefix] = {
        'region': value['properties']['region'],
        'platform': value['properties']['platform'],
        'systemService': value['properties']['systemService'],
        'cloud': result['cloud']
    }

result = azure_parser.get_gov_range()
for value in result['values']:
  for prefix in value['properties']['addressPrefixes']:
    pyt[prefix] = {
        'region': value['properties']['region'],
        'platform': value['properties']['platform'],
        'systemService': value['properties']['systemService'],
        'cloud': result['cloud']
    }

'''
Testing - Azure
{'region': '', 'platform': 'Azure', 'systemService': '', 'cloud': 'Public'}
{'region': '', 'platform': 'Azure', 'systemService': 'AzureAppConfiguration', 'cloud': 'AzureGovernment'}
'''
# print(pyt.get('213.199.183.0'))
# print(pyt.get('52.127.61.112'))
