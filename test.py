import json
import pytricia

from src.reader import FileReader
from src.dl.download_zoom import ZoomCidrDownloader

from src.pytrie_support import PytrieSupport
from src.whois import whois


def run_test():
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
  data = reader.read('data/raw/zoom-contact-center.txt')                   
  support.add_zoom_cidr(pyt, data,
                        zoom.get_config().get('source').get('cc'),
                        zoom.get_config().get('url').get('cc'))
  data = reader.read('data/raw/zoom-cdn.txt')
  support.add_zoom_cidr(pyt, data,
                        zoom.get_config().get('source').get('cdn'),
                        zoom.get_config().get('url').get('cdn'))
  data = reader.read('data/raw/datadog.json')
  support.add_datadog_cidr(pyt, json.loads(data))

  # data = reader.read('data/raw/github.json')
  # support.add_github_cidr(pyt, json.loads(data))

  data = reader.read('data/raw/atlassian.json')
  support.add_atlassian_cidr(pyt, json.loads(data))

  data = reader.read('data/raw/pingdom-ipv4.txt')
  support.add_pingdom_cidr(pyt, data)

  data = reader.read('data/raw/pingdom-ipv6.txt')
  support.add_pingdom_cidr(pyt, data)

  data = reader.read('data/raw/digitalocean.txt')
  support.add_digitalocean_cidr(pyt, data)

  data = reader.read('data/raw/linode.txt')
  support.add_linode_cidr(pyt, data)

  data = reader.read('data/raw/maxcdn.txt')
  support.add_maxcdn_cidr(pyt, data)

  data = reader.read('data/raw/grafana-hosted-alerts.txt')
  support.add_grafana_cidr(pyt, data, 'hosted alerts')
  data = reader.read('data/raw/grafana-hosted-logs.txt')
  support.add_grafana_cidr(pyt, data, 'hosted logs')
  data = reader.read('data/raw/grafana-hosted-metrics.txt')
  support.add_grafana_cidr(pyt, data, 'hosted metrics')
  data = reader.read('data/raw/grafana-hosted-traces.txt')
  support.add_grafana_cidr(pyt, data, 'hosted traces')
  data = reader.read('data/raw/grafana-hosted.txt')
  support.add_grafana_cidr(pyt, data, 'hosted grafana')
  data = reader.read('data/raw/grafana-synthetic-monitoring.json')
  support.add_grafana_synthetics(pyt, json.loads(data), 'grafana synthetic monitoring')

  '''
    Testing - AWS
    {'region': 'us-east-1', 'service': 'EC2'}
    {'region': 'eu-west-2', 'service': 'S3'}
  '''
  print(pyt.get('52.95.245.0'))
  print(pyt.get('2a05:d07a:c000::'))
  print(pyt.get('18.253.194.205'))

  '''
    Testing - Azure
    {'region': '', 'platform': 'Azure', 'systemService': '', 'cloud': 'Public'}
    {'region': '', 'platform': 'Azure',
        'systemService': 'AzureAppConfiguration', 'cloud': 'AzureGovernment'}
  '''
  print(pyt.get('213.199.183.0'))
  print(pyt.get('52.127.61.112'))

  '''
  Testing - Google
  '''
  # print(pyt.get('35.199.128.0'))
  # print(pyt.get('35.200.0.0'))

  '''
  Testing - Cloudflare
  '''
  print(pyt.get('108.162.192.0'))
  print(pyt.get('2c0f:f248::'))

  '''
  Testing - Fastly
  '''
  print(pyt.get('23.235.32.0'))
  print(pyt.get('2a04:4e40::'))
  print(pyt.get('2c0f:f248::'))

  '''
  Testing - Zoom
  '''
  print(pyt.get('13.32.101.253'))
  print(pyt.get('3.208.72.0/32'))
  print(pyt.get('204.80.104.0'))
  '''
  Testing - Datadog
  '''

  print(pyt.get('13.115.46.213/32'))
  print(pyt.get('63.35.33.198/32'))
  print(pyt.get('3.233.144.0/20'))
  print(pyt.get('99.79.87.237/32'))

  print(pyt.get(pyt.parent('13.115.46.213/32')))
  print(pyt.get(pyt.parent('63.35.33.198/32')))
  print(pyt.get(pyt.parent('3.233.144.0/20')))
  print(pyt.get(pyt.parent('99.79.87.237/32')))

  '''
  Testing - Github
  '''
  # print(pyt.get('13.229.188.59/32'))
  # print(pyt.get('13.67.153.67'))

  '''
  Testing - Atlassian
  '''
  print(pyt.get('18.184.99.128/25'))
  print(pyt.get(pyt.parent('18.184.99.128/25')))

  '''
  Testing - Pingdom
  '''
  print(pyt.get('43.229.84.12'))
  print(pyt.get('2a02:6ea0:c305::4041'))

  '''
  Testing - Digital Ocean
  '''
  print(pyt.get('45.55.192.0'))

  '''
  Testing - Linode
  '''
  print(pyt.get('72.14.177.0'))

  '''
  Testing - MaxCDN
  '''
  print(pyt.get('108.168.175.204'))

  '''
  Testing - Grafana
  '''
  print(pyt.get('35.227.211.64'))
  print(pyt.get('13.245.152.138'))

  '''
  Testing - Whois
  '''
  print(whois('1.1.1.1'))


def main():
  '''
  Test it out!
  '''
  run_test()


if __name__ == "__main__":
  main()
