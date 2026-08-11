## OpenAI publishes the IP ranges used by its web crawlers directly as JSON.
## Documentation: https://platform.openai.com/docs/bots

import requests


class OpenAICidrDownloader():

  def get_config(self):
    config = [
      {
        "for": "OpenAI GPTBot (training crawler)",
        "url": "https://openai.com/gptbot.json",
        "name": "openai-gptbot.json"
      },
      {
        "for": "OpenAI ChatGPT-User (plugin/browsing on behalf of a user)",
        "url": "https://openai.com/chatgpt-user.json",
        "name": "openai-chatgpt-user.json"
      },
      {
        "for": "OpenAI OAI-SearchBot (search crawler)",
        "url": "https://openai.com/searchbot.json",
        "name": "openai-searchbot.json"
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
      print(f"Failure to scrape OpenAI IP range endpoint for {info['for']}, error was {e}")
      return None
