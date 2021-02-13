'''
A simple support class for reusing adding to a pytrie object based on
different schema of files provided.
'''

import collections


class PytrieSupport():

  def add_aws_cidr(self, pytrie, result):
    for prefix in result['prefixes']:
      ip = prefix['ip_prefix']
      region = prefix['region']
      service = prefix['service']
      if pytrie.has_key(ip):
        tri_result = pytrie.get(ip)
        region = f"{region},{tri_result['region']}"
        service = f"{service},{tri_result['service']}"
      pytrie[ip] = {
          'region': region,
          'service': service,
          'createDate': result['createDate']
      }

    for prefix in result['ipv6_prefixes']:
      ip = prefix['ipv6_prefix']
      region = prefix['region']
      service = prefix['service']
      if pytrie.has_key(ip):
        tri_result = pytrie.get(ip)
        region = f"{region},{tri_result['region']}"
        service = f"{service},{tri_result['service']}"
      pytrie[ip] = {
          'region': region,
          'service': service,
          'createDate': result['createDate']
      }

  def add_azure_cidr(self, pytrie, result):
    for value in result['values']:
      for prefix in value['properties']['addressPrefixes']:
        region = value['properties']['region']
        platform = value['properties']['platform']
        systemService = value['properties']['systemService']
        cloud = result['cloud']

        if pytrie.has_key(prefix):
          tri_result = pytrie.get(prefix)
          if tri_result['region'] != "":
            region = tri_result['region']
          if tri_result['platform'] != "":
            platform = tri_result['platform']
          if tri_result['systemService'] != "":
            systemService = tri_result['systemService']

        pytrie[prefix] = {
            'region': region,
            'platform': platform,
            'systemService': systemService,
            'cloud': cloud,
            'changeNumber': result['changeNumber'],
            'createDate': result['createDate']
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

  def add_datadog_cidr(self, pytrie, result):
    version = result['version']
    modified = result['modified']
    source = 'Datadog'
    website = 'https://ip-ranges.datadoghq.com/'
    for integration, iptables in result.items():
      if isinstance(iptables, collections.Mapping):
        if 'prefixes_ipv4_by_location' in iptables:
          for location, ipv4s in iptables.get('prefixes_ipv4_by_location', []).items():
            for ipv4 in ipv4s:
              pytrie[ipv4] = {
                  'source': source,
                  'website': website,
                  'version': version,
                  'modified': modified,
                  'location': location,
                  'integration': integration
              }
        if 'prefixes_ipv4_by_location' not in iptables:
          for ipv4 in iptables.get('prefixes_ipv4', []):
            pytrie[ipv4] = {
                'source': source,
                'website': website,
                'version': version,
                'modified': modified,
                'integration': integration
            }
        if 'prefixes_ipv6_by_location' in iptables:
          for location, ipv6s in iptables.get('prefixes_ipv4_by_location', []).items():
            for ipv6 in ipv6s:
              pytrie[ipv6] = {
                  'source': source,
                  'website': website,
                  'version': version,
                  'modified': modified,
                  'location': location,
                  'integration': integration
              }
        if 'prefixes_ipv6_by_location' not in iptables:
          for ipv6 in iptables.get('prefixes_ipv6', []):
            pytrie[ipv6] = {
                'source': source,
                'website': website,
                'version': version,
                'modified': modified,
                'integration': integration
            }
