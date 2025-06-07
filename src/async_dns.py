from dns import resolver
from dns.exception import DNSException

import itertools
import collections
import multiprocessing.pool

def worker(arg):
  """
  query dns for (hostname, qname) and return (qname, [rdata,...])
  """
  try:
    url, qname, nameserver = arg
    custom_resolver = resolver.Resolver()
    # Log progress because this times out on certain government networks.
    custom_resolver.timeout = custom_resolver.lifetime = 5
    custom_resolver.nameservers = [nameserver]
    print(f'Querying {qname} record of {url} from {nameserver}...')
    rdatalist = [rdata for rdata in custom_resolver.resolve(url, qname)]
    print(f'Finished querying {qname} record of {url} from {nameserver}.')
    return(url, rdatalist)
  except DNSException as e:
    print(f'Querying from {nameserver} failed because {e}')
    return(url, [])


def resolve_dns(url_list, nameservers):
  """
  Given a list of hosts, return dict that maps qname to
  returned rdata records.
  """
  response_dict = collections.defaultdict(list)

  # create pool for querys but cap max number of threads
  pool = multiprocessing.pool.ThreadPool(processes=min(len(url_list)*3, 60))

  # run for all combinations of hosts and qnames
  for url, rdatalist in pool.imap(
          worker,
          itertools.product(url_list, ('A', 'AAAA'), nameservers),
          chunksize=1):
    response_dict[url].extend(rdatalist)
  pool.close()
  return response_dict


def resolve_all_dns(urls):
  PUBLIC_NAMESERVERS = ['1.1.1.1']

  # Resolve all URLs here based on responses from the
  # authoratative nameserver.
  resolution = {}
  result = resolve_dns(urls, PUBLIC_NAMESERVERS)
  for url, rdatalist in result.items():
    for rdata in rdatalist:
      if url not in resolution:
        resolution[url] = [rdata.address]
      if rdata.address in resolution[url]:
        continue
      else:
        resolution[url].append(rdata.address)
  return resolution
