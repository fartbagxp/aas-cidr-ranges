'''
Unit tests for the vendor-published collectors sourced from
https://github.com/lord-alfred/ipranges (used here as a discovery aid for
which vendors publish their own IP ranges directly, not as a data source
itself). Every collector under test hits an endpoint published by the
vendor -- no RADB/RIPE whois lookups and no third-party aggregators such as
SecOps-Institute.

HTTP calls are mocked so these tests run offline and deterministically.
'''

import json

import requests

from src.dl.download_bing import BingCidrDownloader
from src.dl.download_duckduckgo import DuckDuckGoCidrDownloader
from src.dl.download_openai import OpenAICidrDownloader
from src.dl.download_perplexity import PerplexityCidrDownloader
from src.dl.download_statuscake import StatusCakeCidrDownloader
from src.dl.download_telegram import TelegramCidrDownloader


class FakeResponse:
    def __init__(self, text='', json_data=None):
        self.text = text
        self._json_data = json_data

    def json(self):
        if self._json_data is None:
            return json.loads(self.text)
        return self._json_data


class TestOpenAI:
    def test_get_range_tags_bot(self, monkeypatch):
        payload = {'creationTime': '2026-01-01', 'prefixes': [{'ipv4Prefix': '203.0.113.0/24'}]}

        def fake_get(url, timeout=30):
            assert url == 'https://openai.com/gptbot.json'
            return FakeResponse(json_data=payload)

        monkeypatch.setattr(requests, 'get', fake_get)

        downloader = OpenAICidrDownloader()
        config = downloader.get_config()
        gptbot = next(c for c in config if c['name'] == 'openai-gptbot.json')
        result = downloader.get_range(gptbot)

        assert result['for'] == gptbot['for']
        assert result['prefixes'] == payload['prefixes']

    def test_get_config_has_three_bots(self):
        downloader = OpenAICidrDownloader()
        names = {c['name'] for c in downloader.get_config()}
        assert names == {
            'openai-gptbot.json',
            'openai-chatgpt-user.json',
            'openai-searchbot.json',
        }

    def test_get_range_returns_none_on_failure(self, monkeypatch):
        def fake_get(url, timeout=30):
            raise requests.exceptions.RequestException('boom')

        monkeypatch.setattr(requests, 'get', fake_get)

        downloader = OpenAICidrDownloader()
        config = downloader.get_config()[0]
        assert downloader.get_range(config) is None


class TestBing:
    def test_get_range(self, monkeypatch):
        payload = {'prefixes': [{'ipv4Prefix': '198.51.100.0/24'}]}

        def fake_get(url, timeout=30):
            assert url == 'https://www.bing.com/toolbox/bingbot.json'
            return FakeResponse(json_data=payload)

        monkeypatch.setattr(requests, 'get', fake_get)

        result = BingCidrDownloader().get_range()
        assert result == payload

    def test_get_range_returns_none_on_failure(self, monkeypatch):
        def fake_get(url, timeout=30):
            raise requests.exceptions.RequestException('boom')

        monkeypatch.setattr(requests, 'get', fake_get)
        assert BingCidrDownloader().get_range() is None


class TestTelegram:
    def test_get_range_splits_ipv4_and_ipv6(self, monkeypatch):
        text = '91.108.56.0/22\n149.154.160.0/20\n2001:b28:f23d::/48\n2a0a:f280::/32\n'

        def fake_get(url, timeout=30):
            assert url == 'https://core.telegram.org/resources/cidr.txt'
            return FakeResponse(text=text)

        monkeypatch.setattr(requests, 'get', fake_get)

        result = TelegramCidrDownloader().get_range()
        assert result['ipv4'] == ['149.154.160.0/20', '91.108.56.0/22']
        assert result['ipv6'] == ['2001:b28:f23d::/48', '2a0a:f280::/32']

    def test_get_range_returns_none_on_failure(self, monkeypatch):
        def fake_get(url, timeout=30):
            raise requests.exceptions.RequestException('boom')

        monkeypatch.setattr(requests, 'get', fake_get)
        assert TelegramCidrDownloader().get_range() is None


class TestDuckDuckGo:
    def test_get_config_has_two_bots(self):
        names = {c['name'] for c in DuckDuckGoCidrDownloader().get_config()}
        assert names == {
            'duckduckgo-duckduckbot.json',
            'duckduckgo-duckassistbot.json',
        }

    def test_get_range_tags_bot(self, monkeypatch):
        payload = {'prefixes': [{'ipv4Prefix': '104.43.54.127/32'}]}

        def fake_get(url, timeout=30):
            assert url == 'https://duckduckgo.com/duckduckbot.json'
            return FakeResponse(json_data=payload)

        monkeypatch.setattr(requests, 'get', fake_get)

        downloader = DuckDuckGoCidrDownloader()
        config = next(c for c in downloader.get_config() if c['name'] == 'duckduckgo-duckduckbot.json')
        result = downloader.get_range(config)
        assert result['for'] == config['for']
        assert result['prefixes'] == payload['prefixes']


class TestPerplexity:
    def test_get_config_has_two_bots(self):
        names = {c['name'] for c in PerplexityCidrDownloader().get_config()}
        assert names == {
            'perplexity-perplexitybot.json',
            'perplexity-user.json',
        }

    def test_get_range_tags_bot(self, monkeypatch):
        payload = {'prefixes': [{'ipv4Prefix': '107.20.236.150/32'}]}

        def fake_get(url, timeout=30):
            assert url == 'https://www.perplexity.ai/perplexitybot.json'
            return FakeResponse(json_data=payload)

        monkeypatch.setattr(requests, 'get', fake_get)

        downloader = PerplexityCidrDownloader()
        config = next(c for c in downloader.get_config() if c['name'] == 'perplexity-perplexitybot.json')
        result = downloader.get_range(config)
        assert result['for'] == config['for']
        assert result['prefixes'] == payload['prefixes']


class TestStatusCake:
    def test_get_range(self, monkeypatch):
        text = '146.190.20.113\n198.211.123.207\n'

        def fake_get(url, timeout=30):
            assert url == 'https://app.statuscake.com/Workfloor/Locations.php?format=txt'
            return FakeResponse(text=text)

        monkeypatch.setattr(requests, 'get', fake_get)

        result = StatusCakeCidrDownloader().get_range()
        assert result == text

    def test_get_range_returns_none_on_failure(self, monkeypatch):
        def fake_get(url, timeout=30):
            raise requests.exceptions.RequestException('boom')

        monkeypatch.setattr(requests, 'get', fake_get)
        assert StatusCakeCidrDownloader().get_range() is None
