'''
Google Cloud Compute for IP ranges:
https://cloud.google.com/compute/docs/faq#find_ip_range

Script for finding all CIDRs:
https://gist.github.com/n0531m/f3714f6ad6ef738a3b0a
'''
import json


class GoogleCIDRParser():
  def get_range(self):
    with open('data/gcp.json') as f:
      data = json.load(f)
      return data
