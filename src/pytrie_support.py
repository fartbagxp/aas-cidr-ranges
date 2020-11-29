'''
A simple support class for reusing adding to a pytrie object based on 
different schema of files provided.
'''


class PytrieSupport():

  def add_aws_cidr(self, pytrie, result):
    for prefix in result['prefixes']:
      pytrie[prefix['ip_prefix']] = {
          'region': prefix['region'],
          'service': prefix['service']
      }

    for prefix in result['ipv6_prefixes']:
      pytrie[prefix['ipv6_prefix']] = {
          'region': prefix['region'],
          'service': prefix['service']
      }

  def add_azure_cidr(self, pytrie, result):
    for value in result['values']:
      for prefix in value['properties']['addressPrefixes']:
        pytrie[prefix] = {
            'region': value['properties']['region'],
            'platform': value['properties']['platform'],
            'systemService': value['properties']['systemService'],
            'cloud': result['cloud']
        }

  def add_gcp_cidr(self, pytrie, result):
    results = result.split('\n')
    for r in results:
      if r.strip():
        pytrie[r] = {
            'source': 'Google',
            'website': '_cloud-netblocks.googleusercontent.com'
        }

  def add_zoom_cidr(self, pytrie, result, source, website):
    results = result.split('\n')
    for r in results:
      if r.strip():
        pytrie[r] = {
            'source': source,
            'website': website
        }

  def add_cloudflare_cidr(self, pytrie, result):
    results = result.split('\n')
    for r in results:
      if r.strip():
        pytrie[r] = {
            'source': 'Cloudflare',
            'website': 'https://www.cloudflare.com/ips/'
        }

  def add_fastly_cidr(self, pytrie, result):
    for ipv4 in result['addresses']:
      pytrie[ipv4] = {
          'source': 'Fastly',
          'website': 'https://api.fastly.com/public-ip-list'
      }
    for ipv6 in result['ipv6_addresses']:
      pytrie[ipv6] = {
          'source': 'Fastly',
          'website': 'https://api.fastly.com/public-ip-list'
      }
