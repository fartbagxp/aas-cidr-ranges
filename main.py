import json
import ipaddress
import pytricia

from src.reader import FileReader
from src.dl.download_zoom import ZoomCidrDownloader
from src.pytrie_support import PytrieSupport

'''
Provides an entry point to a job for providing results about a particular
IP address or range.
'''


def handler(event):

  if 'ip' not in event:
    return {
        'statusCode': 400,
        'error': "Request must have field 'ip' with value of an IP address or valid CIDR notation"
    }

  isValidParameter = False
  try:
    ipaddress.ip_address(event['ip'])
    isValidParameter = True
  except ValueError:
    pass

  try:
    ipaddress.ip_network(event['ip'])
    isValidParameter = True
  except ValueError:
    pass

  if isValidParameter == False:
    return {
        'statusCode': 400,
        'error': "Request must have field 'ip' with value of an IP address or valid CIDR notation"
    }

  # 128 bits needed for holding IPv6
  pyt = pytricia.PyTricia(128)
  support = PytrieSupport()

  # read all the files locally
  reader = FileReader()
  data = reader.read('data/raw/aws.json')
  support.add_aws_cidr(pyt, json.loads(data))

  data = reader.read('data/raw/azure-public.json')
  support.add_azure_cidr(pyt, json.loads(data))

  data = reader.read('data/raw/azure-china.json')
  support.add_azure_cidr(pyt, json.loads(data))

  data = reader.read('data/raw/azure-germany.json')
  support.add_azure_cidr(pyt, json.loads(data))

  data = reader.read('data/raw/azure-gov.json')
  support.add_azure_cidr(pyt, json.loads(data))

  data = reader.read('data/raw/gcp.txt')
  support.add_gcp_cidr(pyt, data)

  data = reader.read('data/raw/cloudflare-ipv4.txt')
  support.add_cloudflare_cidr(pyt, data)

  data = reader.read('data/raw/cloudflare-ipv6.txt')
  support.add_cloudflare_cidr(pyt, data)

  data = reader.read('data/raw/fastly.json')
  support.add_fastly_cidr(pyt, json.loads(data))

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

  result = pyt.get(event['ip'])
  if result == None:
    return {
        'statusCode': 200,
        'data': {},
        'error': 'No available information'
    }

  return {
      'statusCode': 200,
      'data': result
      'error': ''
  }


def main():
  result = handler({'ip': '127.0.0.1'})
  print(result)
  result = handler({'ip': '213.199.183.0'})
  print(result)
  result = handler({'ip': '35.180.0.0/24'})
  print(result)


if __name__ == "__main__":
  main()
