
import json

# TODO: scrape the Zoom document for their IP address range:
# https://srome.github.io/Parsing-HTML-Tables-in-Python-with-BeautifulSoup-and-pandas/


class ZoomCIDRParser():
  def get_range(self):
    with open('data/zoom.json') as f:
      data = json.load(f)
      return data
