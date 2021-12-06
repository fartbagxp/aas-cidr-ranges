import json
import ipaddress
import pytricia

from src.reader import FileReader
from src.dl.download_zoom import ZoomCidrDownloader
from src.pytrie_support import PytrieSupport

from src.whois import whois


def sanitize_parameter(event):
  body = {
      'error': '',
      'data': {}
  }

  result = {
      'statusCode': 200,
      'body': {}
  }

  isValid = True

  if 'queryStringParameters' not in event:
    isValid = False
    body['error'] = "Request must have field 'ip' with value of an IP address or valid CIDR notation"
    result = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

  if event['queryStringParameters'] is None or 'ip' not in event['queryStringParameters']:
    isValid = False
    body['error'] = "Request must have field 'ip' with value of an IP address or valid CIDR notation"
    result = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

  return isValid, body, result


def get_ip_info(pytries, ip):
  results = []

  for pyt in pytries:
    try:
      result = pyt.get(ip)
      if result:
        results.append(result)
    except KeyError:
      pass

  try:
    parent_ip = pyt.parent(ip)
    for pyt in pytries:
      result = pyt.get(parent_ip)
      if result:
        results.append(result)
  except:
    pass

  ip_info = {
      'request_ip': ip,
      'environments': results,
  }

  return ip_info


def generate_reader():
  pytries = []

  # loader for each of the specific file in the format needed
  support = PytrieSupport()
  reader = FileReader()

  # 128 bits needed for holding IPv6
  pyt = pytricia.PyTricia(128)
  data = reader.read('data/raw/aws.json')
  support.add_aws_cidr(pyt, json.loads(data))
  pytries.append(pyt)

  pyt = pytricia.PyTricia(128)
  data = reader.read('data/raw/azure-public.json')
  support.add_azure_cidr(pyt, json.loads(data))
  pytries.append(pyt)

  data = reader.read('data/raw/azure-china.json')
  support.add_azure_cidr(pyt, json.loads(data))

  data = reader.read('data/raw/azure-germany.json')
  support.add_azure_cidr(pyt, json.loads(data))

  data = reader.read('data/raw/azure-gov.json')
  support.add_azure_cidr(pyt, json.loads(data))

  pyt = pytricia.PyTricia(128)
  data = reader.read('data/raw/gcp.txt')
  support.add_gcp_cidr(pyt, data)
  pytries.append(pyt)

  pyt = pytricia.PyTricia(128)
  data = reader.read('data/raw/cloudflare-ipv4.txt')
  support.add_cloudflare_cidr(pyt, data)

  data = reader.read('data/raw/cloudflare-ipv6.txt')
  support.add_cloudflare_cidr(pyt, data)
  pytries.append(pyt)

  pyt = pytricia.PyTricia(128)
  data = reader.read('data/raw/fastly.json')
  support.add_fastly_cidr(pyt, json.loads(data))
  pytries.append(pyt)

  pyt = pytricia.PyTricia(128)
  zoom = ZoomCidrDownloader()
  data = reader.read('data/raw/zoom-crc.txt')
  support.add_zoom_cidr(pyt, data,
                        zoom.get_config().get('source').get('zoom'),
                        zoom.get_config().get('url').get('zoom'))
  data = reader.read('data/raw/zoom-meeting.txt')
  support.add_zoom_cidr(pyt, data,
                        zoom.get_config().get('source').get('meeting'),
                        zoom.get_config().get('url').get('meeting'))
  data = reader.read('data/raw/zoom-phone.txt')
  support.add_zoom_cidr(pyt, data,
                        zoom.get_config().get('source').get('phone'),
                        zoom.get_config().get('url').get('phone'))
  data = reader.read('data/raw/zoom-range.txt')
  support.add_zoom_cidr(pyt, data,
                        zoom.get_config().get('source').get('range'),
                        zoom.get_config().get('url').get('range'))
  pytries.append(pyt)

  pyt = pytricia.PyTricia(128)
  data = reader.read('data/raw/datadog.json')
  support.add_datadog_cidr(pyt, json.loads(data))
  pytries.append(pyt)

  pyt = pytricia.PyTricia(128)
  data = reader.read('data/raw/atlassian.json')
  support.add_atlassian_cidr(pyt, json.loads(data))
  pytries.append(pyt)

  pyt = pytricia.PyTricia(128)
  data = reader.read('data/raw/pingdom-ipv4.txt')
  support.add_pingdom_cidr(pyt, data)

  data = reader.read('data/raw/pingdom-ipv6.txt')
  support.add_pingdom_cidr(pyt, data)
  pytries.append(pyt)

  pyt = pytricia.PyTricia(128)
  data = reader.read('data/raw/github.json')
  support.add_github_cidr(pyt, json.loads(data))
  pytries.append(pyt)

  pyt = pytricia.PyTricia(128)
  data = reader.read('data/raw/digitalocean.txt')
  support.add_digitalocean_cidr(pyt, data)
  pytries.append(pyt)

  pyt = pytricia.PyTricia(128)
  data = reader.read('data/raw/linode.txt')
  support.add_linode_cidr(pyt, data)
  pytries.append(pyt)

  return pytries


'''
Provides an entry point to a job for providing results about a particular
IP address or range.
'''


def belong(event, context):
  isValid, body, results = sanitize_parameter(event)
  if isValid is False:
    return results

  ip = event['queryStringParameters']['ip']
  print(ip)

  isValidParameter = False
  isValidIP = False
  isValidCIDR = False
  try:
    ipaddress.ip_address(ip)
    isValidParameter = True
    isValidIP = True
  except ValueError:
    pass

  try:
    ipaddress.ip_network(ip)
    isValidParameter = True
    isValidCIDR = True
  except ValueError:
    pass

  if isValidParameter == False:
    body['error'] = "Request must have field 'ip' with value of an IP address or valid CIDR notation"
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }

  pytries = generate_reader()
  result = get_ip_info(pytries, ip)
  if result != None:
    body['error'] = ''
    body['data'] = result
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }

  if result == None and isValidIP is True:
    body['error'] = ''
    body['data'] = whois(ip)
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }

  body['error'] = 'No available information'
  return {
      'statusCode': 200,
      'body': json.dumps(body)
  }


def main():
  result = belong({'queryStringParameters': {
      'ip': '100.100.100.100'}}, None)
  print(result)
  result = belong({'queryStringParameters': {'ip': '20.140.48.160'}}, None)
  print(result)
  result = belong({'queryStringParameters': {'ip': '213.199.183.0'}}, None)
  print(result)
  result = belong({'queryStringParameters': {'ip': '35.180.0.0/24'}}, None)
  print(result)
  result = belong({'queryStringParameters': {'ip': '35.180.0.265'}}, None)
  print(result)
  result = belong({'queryStringParameters': {'ip': '13.115.46.213/32'}}, None)
  print(result)
  result = belong({'queryStringParameters': {'ip': '140.82.114.3'}}, None)
  print(result)
  result = belong({'queryStringParameters': {'ip': '18.229.199.252/32'}}, None)
  print(result)


if __name__ == "__main__":
  main()
