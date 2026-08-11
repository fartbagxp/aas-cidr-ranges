## Perplexity publishes the IP ranges used by its own crawlers directly as JSON.
## Documentation: https://docs.perplexity.ai/guides/bots

import requests


class PerplexityCidrDownloader():

  def get_config(self):
    config = [
      {
        "for": "PerplexityBot (search crawler)",
        "url": "https://www.perplexity.ai/perplexitybot.json",
        "name": "perplexity-perplexitybot.json"
      },
      {
        "for": "Perplexity-User (browsing on behalf of a user)",
        "url": "https://www.perplexity.ai/perplexity-user.json",
        "name": "perplexity-user.json"
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
      print(f"Failure to scrape Perplexity IP range endpoint for {info['for']}, error was {e}")
      return None
