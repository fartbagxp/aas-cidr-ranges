import requests

class StripeCidrDownloader():

  def get_api_ip(self):
    try:
      URL = 'https://stripe.com/files/ips/ips_api.txt'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Stripe IP range endpoint, error was {e}')
      return None

  def get_webhook_ip(self):
    try:
      URL = 'https://stripe.com/files/ips/ips_webhooks.txt'
      r = requests.get(url=URL)
      data = r.text
      return data
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Stripe IP range endpoint, error was {e}')
      return None
