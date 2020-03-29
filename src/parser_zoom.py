
import json


class ZoomCIDRParser():
  def get_range(self):
    with open('data/zoom.json') as f:
      data = json.load(f)
      return data
