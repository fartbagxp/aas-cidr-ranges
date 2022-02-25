import json
from src.dl.download_aws import AWSCidrDownloader
from src.dl.download_azure import AzureCidrDownloader
from src.dl.download_zoom import ZoomCidrDownloader
from src.dl.download_cloudflare import CloudflareCidrDownloader
from src.dl.download_fastly import FastlyCidrDownloader
from src.dl.download_datadog import DatadogCidrDownloader
from src.dl.download_google import GcpCidrDownloader
from src.dl.download_github import GithubCidrDownloader
from src.dl.download_atlassian import AtlassianCidrDownloader
from src.dl.download_pingdom import PingdomCidrDownloader
from src.dl.download_digitalocean import DigitalOceanCidrDownloader
from src.dl.download_linode import LinodeCidrDownloader
from src.dl.download_maxcdn import MaxCDNCidrDownloader
from src.dl.download import CidrWriter

'''
The updater saves the raw IP data from the source to the local repository
so we can analyze it later, whenever we want.

This can be run independently from the handler.py and test.py.
'''


def update():
  writer = CidrWriter()

  aws_downloader = AWSCidrDownloader()
  result = aws_downloader.get_range()
  writer.write('data/raw/aws.json', json.dumps(result, indent=2))

  azure_downloader = AzureCidrDownloader()
  result = azure_downloader.get_public_range()
  writer.write('data/raw/azure-public.json', json.dumps(result, indent=2))

  result = azure_downloader.get_china_range()
  writer.write('data/raw/azure-china.json', json.dumps(result, indent=2))

  result = azure_downloader.get_germany_range()
  writer.write('data/raw/azure-germany.json', json.dumps(result, indent=2))

  result = azure_downloader.get_gov_range()
  writer.write('data/raw/azure-gov.json', json.dumps(result, indent=2))

  cloudflare_downloader = CloudflareCidrDownloader()
  result = cloudflare_downloader.get_range_v4()
  writer.write('data/raw/cloudflare-ipv4.txt', result)

  result = cloudflare_downloader.get_range_v6()
  writer.write('data/raw/cloudflare-ipv6.txt', result)

  fastly_downloader = FastlyCidrDownloader()
  result = fastly_downloader.get_range()
  writer.write('data/raw/fastly.json', json.dumps(result, indent=2))

  zoom_downloader = ZoomCidrDownloader()
  result, source, website = zoom_downloader.get_zoom_range()
  writer.write('data/raw/zoom-range.txt', result)

  result, source, website = zoom_downloader.get_zoom_meeting_range()
  writer.write('data/raw/zoom-meeting.txt', result)

  result, source, website = zoom_downloader.get_zoom_crc_range()
  writer.write('data/raw/zoom-crc.txt', result)

  result, source, website = zoom_downloader.get_zoom_phone_range()
  writer.write('data/raw/zoom-phone.txt', result)

  result, source, website = zoom_downloader.get_zoom_phone_range()
  writer.write('data/raw/zoom-phone.txt', result)

  datadog_downloader = DatadogCidrDownloader()
  result = datadog_downloader.get_range()
  writer.write('data/raw/datadog.json', json.dumps(result, indent=2))

  github_downloader = GithubCidrDownloader()
  result = github_downloader.get_range()
  writer.write('data/raw/github.json', json.dumps(result, indent=2))

  google_downloader = GcpCidrDownloader()
  result = google_downloader.get_range()
  writer.write('data/raw/gcp.json', json.dumps(result, indent=2))

  atlassian_downloader = AtlassianCidrDownloader()
  result = atlassian_downloader.get_range()
  writer.write('data/raw/atlassian.json', json.dumps(result, indent=2))

  pingdom_downloader = PingdomCidrDownloader()
  result = pingdom_downloader.get_range_v4()
  writer.write('data/raw/pingdom-ipv4.txt', result)

  result = pingdom_downloader.get_range_v6()
  writer.write('data/raw/pingdom-ipv6.txt', result)

  digitalocean_downloader = DigitalOceanCidrDownloader()
  result = digitalocean_downloader.get_range()
  writer.write('data/raw/digitalocean.txt', result)

  linode_downloader = LinodeCidrDownloader()
  result = linode_downloader.get_range()
  writer.write('data/raw/linode.txt', result)

  maxcdn_downloader = MaxCDNCidrDownloader()
  result = maxcdn_downloader.get_range()
  writer.write('data/raw/maxcdn.txt', result)

def main():
  update()


if __name__ == "__main__":
  main()
