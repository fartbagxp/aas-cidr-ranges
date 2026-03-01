'''
A simple support class for reusing adding to a pytrie object based on
different schema of files provided.

Essentially, this is a collection of parsers on parsing the various files and
inputting it into the IP trie.
'''
import ipaddress

class PytrieSupport():

  def validate_ip_address(self, address):
    try:
      try:
        ipaddress.ip_address(address)
        # if isinstance(ip, ipaddress.IPv4Address):
        #   print("{} is an IPv4 address".format(address))
        # elif isinstance(ip, ipaddress.IPv6Address):
        #   print("{} is an IPv6 address".format(address))
        return True
      except ValueError:
        ipaddress.ip_network(address)
        # if isinstance(ip, ipaddress.IPv4Network):
        #   print("{} is an IPv4 network".format(address))
        # elif isinstance(ip, ipaddress.IPv6Network):
        #   print("{} is an IPv6 network".format(address))
        return True
    except ValueError:
      # print("IP address {} is not valid".format(address))
      return False

  def add_atlassian_cidr(self, pytrie, result):
    for items in result['items']:
      for item in items:
        ip = items['cidr']
        if ip is not None:
          pytrie[ip] = {
              'source': 'Atlassian',
              'website': 'https://ip-ranges.atlassian.com/'
          }

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
      try:
        if 'prefixes_ipv4' in iptables:
          for ipv4 in iptables.get('prefixes_ipv4', []):
            pytrie[ipv4] = {
                'source': source,
                'website': website,
                'version': version,
                'modified': modified,
                'integration': integration
            }
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
        if 'prefixes_ipv6' in iptables:
          for ipv6 in iptables.get('prefixes_ipv6', []):
            pytrie[ipv6] = {
                'source': source,
                'website': website,
                'version': version,
                'modified': modified,
                'integration': integration
            }
      except TypeError:
        # print("Exception caught: unable to parse a number as iptables in Datadog")
        pass

  def add_digitalocean_cidr(self, pytrie, result):
    lines = result.split('\n')
    for r in lines:
      r = r.strip()
      if r:
        items = r.split(',')
        if len(items) < 5:
          continue
        cidr = items[0]
        country = items[1]
        subdivision = items[2]
        city = items[3]
        zipcode = items[4]

        pytrie[cidr] = {
          'source': 'DigitalOcean',
          'website': 'https://digitalocean.com/geo/google.csv',
          'country': country,
          'subdivision': subdivision,
          'city': city,
          'zipcode': zipcode
        }

  def add_gcp_cidr(self, pytrie, result):
    results = result.split('\n')
    for r in results:
      if r.strip():
        pytrie[r] = {
            'source': 'Google',
            'website': 'https://cloud.google.com/compute/docs/faq'
        }

  def add_github_cidr(self, pytrie, result):
    for key in result:
      if isinstance(result[key], list):
        for ip in result[key]:
          ip = ip.strip()
          if self.validate_ip_address(ip):
            pytrie[ip] = {
                'source': 'Github',
                'product': key,
                'website': 'https://help.github.com/en/github/authenticating-to-github/about-githubs-ip-addresses'
            }

  def add_grafana_cidr(self, pytrie, result, service):
    results = result.split('\n')
    for r in results:
      if r.strip():
        pytrie[r] = {
            'source': 'Grafana',
            'service': service,
            'website': 'https://grafana.com/docs/grafana-cloud/reference/allow-list/'
        }

  def add_grafana_synthetics(self, pytrie, result, service):
    for r in result:
      for ip in result[r]:
        pytrie[ip] = {
            'source': 'Grafana',
            'service': service,
            'url': r,
            'website': 'https://grafana.com/docs/grafana-cloud/reference/allow-list/'
        }

  def add_iana_cidr(self, pytrie, result):
    lines = result.split('\n')
    for r in lines:
      r = r.strip()
      if r and r.startswith('#') is False:
        items = r.split(',')
        # prefix = items[0]
        country = items[1]
        subdivision = items[2]
        city = items[3]
        zipcode = items[4]
        allocation_size = items[5]

        pytrie[r] = {
          'source': 'Linode',
          'website': 'https://geoip.linode.com/',
          'country': country,
          'subdivision': subdivision,
          'city': city,
          'zipcode': zipcode,
          'allocation_size': allocation_size
        }

  def add_linode_cidr(self, pytrie, result):
    lines = result.split('\n')
    for r in lines:
      r = r.strip()
      if r and r.startswith('#') is False:
        items = r.split(',')
        prefix = items[0]
        alpha2code = items[1]
        region = items[2]
        city = items[3]
        zipcode = items[4]
        pytrie[r] = {
          'source': 'Linode',
          'website': 'https://geoip.linode.com/',
          'alpha2code': alpha2code,
          'prefix': prefix,
          'region': region,
          'city': city,
          'zipcode': zipcode
        }

  def add_maxcdn_cidr(self, pytrie, result):
    results = result.split('\n')
    for r in results:
      if r.strip():
        pytrie[r] = {
            'source': 'MaxCDN',
            'website': 'https://support.maxcdn.com/hc/en-us/articles/360036932271-IP-Blocks'
        }

  def add_okta_cidr(self, pytrie, result):
    for r in result:
      ips = result[r].get('ip_ranges', [])
      for ip in ips:
        pytrie[ip] = {
            'source': 'Okta',
            'url': r,
            'website': 'https://s3.amazonaws.com/okta-ip-ranges/ip_ranges.json'
        }

  def add_oracle_cidr(self, pytrie, result):
    timestamp = result.get('last_updated_timestamp','')
    regions = result.get('regions',[])
    for r in regions:
      region_name = r.get('region', '')
      cidrs = r.get('cidrs', [])
      for cidr_info in cidrs:
        cidr = cidr_info.get('cidr', '')
        tags = cidr_info.get('tags', [])
        tags = ','.join(tags)
        pytrie[cidr] = {
            'source': 'Oracle',
            'region_name': region_name,
            'tags': tags,
            'website': 'https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json',
            'updated_timestamp': timestamp
        }

  def add_stripe_cidr(self, pytrie, result):
    results = result.split('\n')
    for r in results:
      if r.strip():
        pytrie[r] = {
            'source': 'Stripe',
            'website': 'https://stripe.com/docs/ips'
        }

  def add_pingdom_cidr(self, pytrie, result):
    results = result.split('\n')
    for r in results:
      if r.strip():
        pytrie[r] = {
            'source': 'Pingdom',
            'website': 'https://documentation.solarwinds.com/en/Success_Center/pingdom/content/topics/pingdom-probe-servers-ip-addresses.htm'
        }

  def add_zoom_cidr(self, pytrie, result, source, website):
    results = result.split('\n')
    for r in results:
      if r.strip():
        pytrie[r] = {
            'source': source,
            'website': website
        }
