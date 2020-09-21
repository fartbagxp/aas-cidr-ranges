import json
from src.download_aws import AWSCidrDownloader
from src.download_azure import AzureCidrDownloader
from src.download_zoom import ZoomCidrDownloader
from src.download_cloudflare import CloudflareCidrDownloader
from src.download_fastly import FastlyCidrDownloader
from src.download import CidrWriter


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

  # gcp_parser = GoogleCidrDownloader()
  # result = gcp_parser.get_range()
  # add_gcp_cidr(pyt, result)

  # '''
  # Testing - Google

  # '''
  # print(pyt.get('35.199.128.0'))
  # print(pyt.get('35.200.0.0'))

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
