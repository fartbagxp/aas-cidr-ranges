## DuckDuckGo publishes the IP ranges used by its own crawlers directly as JSON.
## Documentation:
##   DuckDuckBot:     https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot
##   DuckAssistBot:   https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot

import requests


class DuckDuckGoCidrDownloader():

  def get_config(self):
    config = [
      {
        "for": "DuckDuckBot (search crawler)",
        "url": "https://duckduckgo.com/duckduckbot.json",
        "name": "duckduckgo-duckduckbot.json"
      },
      {
        "for": "DuckAssistBot (AI assist crawler)",
        "url": "https://duckduckgo.com/duckassistbot.json",
        "name": "duckduckgo-duckassistbot.json"
      }
    ]
    return config

  def get_range(self, info):
    try:
      r = requests.get(url=info['url'], timeout=30)
      data = r.json()
      data['for'] = info['for']
      return data
    except requests.exceptions.RequestException as e:
      print(f"Failure to scrape DuckDuckGo IP range endpoint for {info['for']}, error was {e}")
      return None
