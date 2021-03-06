import json
from src.dl.download_aws import AWSCidrDownloader
from src.dl.download_azure import AzureCidrDownloader
from src.dl.download_zoom import ZoomCidrDownloader
from src.dl.download_cloudflare import CloudflareCidrDownloader
from src.dl.download_fastly import FastlyCidrDownloader
from src.dl.download_datadog import DatadogCidrDownloader
from src.dl.download import CidrWriter

'''
The updater saves the raw IP data from the source to the local repository
so we can analyze it later, whenever we want.

This can be run independently from the handler.py and test.py.
'''


def update():
  writer = CidrWriter()

  aws_parser = AWSCidrDownloader()
  result = aws_parser.get_range()
  writer.write('data/raw/aws.json', json.dumps(result, indent=2))

  azure_parser = AzureCidrDownloader()
  result = azure_parser.get_public_range()
  writer.write('data/raw/azure-public.json', json.dumps(result, indent=2))

  result = azure_parser.get_china_range()
  writer.write('data/raw/azure-china.json', json.dumps(result, indent=2))

  result = azure_parser.get_germany_range()
  writer.write('data/raw/azure-germany.json', json.dumps(result, indent=2))

  result = azure_parser.get_gov_range()
  writer.write('data/raw/azure-gov.json', json.dumps(result, indent=2))

  cloudflare_parser = CloudflareCidrDownloader()
  result = cloudflare_parser.get_range_v4()
  writer.write('data/raw/cloudflare-ipv4.txt', result)

  result = cloudflare_parser.get_range_v6()
  writer.write('data/raw/cloudflare-ipv6.txt', result)

  fastly_parser = FastlyCidrDownloader()
  result = fastly_parser.get_range()
  writer.write('data/raw/fastly.json', json.dumps(result, indent=2))

  zoom_parser = ZoomCidrDownloader()
  result, source, website = zoom_parser.get_zoom_range()
  writer.write('data/raw/zoom-range.txt', result)

  result, source, website = zoom_parser.get_zoom_meeting_range()
  writer.write('data/raw/zoom-meeting.txt', result)

  result, source, website = zoom_parser.get_zoom_crc_range()
  writer.write('data/raw/zoom-crc.txt', result)

  result, source, website = zoom_parser.get_zoom_phone_range()
  writer.write('data/raw/zoom-phone.txt', result)

  result, source, website = zoom_parser.get_zoom_phone_range()
  writer.write('data/raw/zoom-phone.txt', result)

  datadog_parser = DatadogCidrDownloader()
  result = datadog_parser.get_range()
  writer.write('data/raw/datadog.json', json.dumps(result, indent=2))


def main():
  update()


if __name__ == "__main__":
  main()
