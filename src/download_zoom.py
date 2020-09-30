
import json
import requests
# from bs4 import BeautifulSoup

'''
List of ranges can be pulled from this Zoom website:
https://support.zoom.us/hc/en-us/articles/201362683-Network-firewall-or-proxy-server-settings-for-Zoom
'''


class ZoomCidrDownloader():

  def __init__(self):
    self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Content-Type': 'text/html',
    }

    self.config = {
        'url': {
            'zoom': 'https://assets.zoom.us/docs/ipranges/Zoom.txt',
            'meeting': 'https://assets.zoom.us/docs/ipranges/ZoomMeetings.txt',
            'crc': 'https://assets.zoom.us/docs/ipranges/ZoomCRC.txt',
            'phone': 'https://assets.zoom.us/docs/ipranges/ZoomPhone.txt'
        },
        'source': {
            'zoom': 'Zoom',
            'meeting': "Zoom Meetings",
            'crc': "Zoom Cloud Room Connector",
            'phone': 'Zoom Phone'
        }
    }

  def get_config(self):
    return self.config

  def get_zoom_range(self):
    try:
      URL = self.config.get('url').get('zoom')
      r = requests.get(url=URL, headers=self.headers)
      data = r.text
      source = self.config.get('source').get('zoom')
      return data, source, URL
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Zoom IP range endpoint, error was {e}')
      return None

  def get_zoom_meeting_range(self):
    try:
      URL = self.config.get('url').get('meeting')
      r = requests.get(url=URL, headers=self.headers)
      data = r.text
      source = self.config.get('source').get('meeting')
      return data, source, URL
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Zoom Meeting IP range endpoint, error was {e}')
      return None

  def get_zoom_crc_range(self):
    try:
      URL = self.config.get('url').get('crc')
      r = requests.get(url=URL, headers=self.headers)
      data = r.text
      source = self.config.get('source').get('crc')
      return data, source, URL
    except requests.exceptions.RequestException as e:
      print(
          f'Failure to scrape Zoom Cloud Room Connector IP range endpoint, error was {e}')
      return None

  def get_zoom_phone_range(self):
    try:
      URL = self.config.get('url').get('phone')
      r = requests.get(url=URL, headers=self.headers)
      data = r.text
      source = self.config.get('source').get('phone')
      return data, source, URL
    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Zoom Phone IP range endpoint, error was {e}')
      return None

  '''
  Example on how to use Beautiful Soup 4 to scrape a HTML table.
  '''
  '''
  def scrape(self):
    try:
      URL = 'https://support.zoom.us/hc/en-us/articles/201362683-Network-firewall-or-proxy-server-settings-for-Zoom'
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
          'Content-Type': 'text/html',
      }
      r = requests.get(url=URL, headers=headers)

      soup = BeautifulSoup(r.text, features="html.parser")
      tables = soup.findAll('table')
      numTables = (len(tables) - 1)

      for table in tables:
        numRows = (len(table.findAll('tr')) - 1)
        for row in table.findAll('tr')[1:numRows]:
          col = row.findAll('td')
          protocol = col[0].getText()
          ports = col[1].getText()
          source = col[2].getText()
          destination = col[3].getText()
          print(protocol, ports, source, destination)
        print('\n\n\n')

    except requests.exceptions.RequestException as e:
      print(f'Failure to scrape Zoom IP range endpoint, error was {e}')
      return None
  '''
