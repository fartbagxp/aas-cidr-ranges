import json
import pytricia

from src.reader import FileReader
from src.dl.download_zoom import ZoomCidrDownloader

from src.pytrie_support import PytrieSupport
from src.whois import whois

from handler import belong

def run_test():

  # '''
  #   Testing - AWS
  #   {'region': 'us-east-1', 'service': 'EC2'}
  #   {'region': 'eu-west-2', 'service': 'S3'}
  # '''
  result = belong({'queryStringParameters': {
      'ip': '52.95.245.0'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '2a05:d07a:c000::'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '18.253.194.205'}}, None)
  print(result)

  # '''
  #   Testing - Azure
  #   {'region': '', 'platform': 'Azure', 'systemService': '', 'cloud': 'Public'}
  #   {'region': '', 'platform': 'Azure',
  #       'systemService': 'AzureAppConfiguration', 'cloud': 'AzureGovernment'}
  # '''
  result = belong({'queryStringParameters': {
      'ip': '213.199.183.0'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '52.127.61.112'}}, None)
  print(result)

  # '''
  # Testing - Google
  # '''
  result = belong({'queryStringParameters': {
      'ip': '35.199.128.0'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '35.200.0.0'}}, None)
  print(result)

  # '''
  # Testing - Cloudflare
  # '''
  result = belong({'queryStringParameters': {
      'ip': '108.162.192.0'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '2c0f:f248::'}}, None)
  print(result)

  # '''
  # Testing - Fastly
  # '''
  result = belong({'queryStringParameters': {
      'ip': '23.235.32.0'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '2a04:4e40::'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '2c0f:f248::'}}, None)
  print(result)

  # '''
  # Testing - Zoom
  # '''
  result = belong({'queryStringParameters': {
      'ip': '13.32.101.253'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '3.208.72.0/32'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '204.80.104.0'}}, None)
  print(result)

  # '''
  # Testing - Datadog
  # '''
  # print(pyt.get('13.115.46.213/32'))
  # print(pyt.get('63.35.33.198/32'))
  # print(pyt.get('3.233.144.0/20'))
  # print(pyt.get('99.79.87.237/32'))
  # print(pyt.get(pyt.parent('13.115.46.213/32')))
  # print(pyt.get(pyt.parent('63.35.33.198/32')))
  # print(pyt.get(pyt.parent('3.233.144.0/20')))
  # print(pyt.get(pyt.parent('99.79.87.237/32')))

  # '''
  # Testing - Github
  # '''
  result = belong({'queryStringParameters': {
      'ip': '13.229.188.59/32'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '13.67.153.67'}}, None)
  print(result)

  # '''
  # Testing - Atlassian
  # '''
  result = belong({'queryStringParameters': {
      'ip': '18.184.99.128/25'}}, None)
  print(result)


  # '''
  # Testing - Pingdom
  # '''
  result = belong({'queryStringParameters': {
      'ip': '43.229.84.12'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '2a02:6ea0:c305::4041'}}, None)
  print(result)

  # '''
  # Testing - Digital Ocean
  # '''
  result = belong({'queryStringParameters': {
      'ip': '45.55.192.0'}}, None)
  print(result)

  # '''
  # Testing - Linode
  # '''
  result = belong({'queryStringParameters': {
      'ip': '72.14.177.0'}}, None)
  print(result)

  # '''
  # Testing - MaxCDN
  # '''
  result = belong({'queryStringParameters': {
      'ip': '108.168.175.204'}}, None)
  print(result)

  # '''
  # Testing - Grafana
  # '''
  result = belong({'queryStringParameters': {
      'ip': '35.227.211.64'}}, None)
  print(result)
  result = belong({'queryStringParameters': {
      'ip': '13.245.152.138'}}, None)
  print(result)

  '''
  Testing - Okta
  '''
  result = belong({'queryStringParameters': {
      'ip': '3.33.185.234'}}, None)
  print(result)

  '''
  Testing - Oracle
  '''
  result = belong({'queryStringParameters': {
      'ip': '129.146.0.0'}}, None)
  print(result)

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
