import json

import pytest

from handler import belong, generate_reader, get_ip_info


@pytest.fixture(scope="module")
def pytries():
    return generate_reader()


def lookup(pytries, ip):
    return get_ip_info(pytries, ip)["environments"]


class TestAWS:
    def test_us_east_1_ipv4(self, pytries):
        envs = lookup(pytries, "52.95.245.0")
        assert any("us-east-1" in e.get("region", "") for e in envs)

    def test_eu_west_2_ipv6(self, pytries):
        envs = lookup(pytries, "2a05:d07a:c000::")
        assert any("eu-west-2" in e.get("region", "") for e in envs)

    def test_gov_cloud(self, pytries):
        envs = lookup(pytries, "18.253.194.205")
        assert len(envs) > 0


class TestAzure:
    def test_public(self, pytries):
        envs = lookup(pytries, "213.199.183.0")
        assert any(
            e.get("platform") == "Azure" and e.get("cloud") == "Public"
            for e in envs
        )

    def test_gov(self, pytries):
        envs = lookup(pytries, "52.127.61.112")
        assert any(
            e.get("platform") == "Azure" and e.get("cloud") == "AzureGovernment"
            for e in envs
        )


class TestGCP:
    def test_ipv4_1(self, pytries):
        envs = lookup(pytries, "35.199.128.0")
        assert any(e.get("source") == "Google" for e in envs)

    def test_ipv4_2(self, pytries):
        envs = lookup(pytries, "35.200.0.0")
        assert any(e.get("source") == "Google" for e in envs)


class TestCloudflare:
    def test_ipv4(self, pytries):
        envs = lookup(pytries, "108.162.192.0")
        assert any(e.get("source") == "Cloudflare" for e in envs)

    def test_ipv6(self, pytries):
        envs = lookup(pytries, "2c0f:f248::")
        assert any(e.get("source") == "Cloudflare" for e in envs)


class TestFastly:
    def test_ipv4(self, pytries):
        envs = lookup(pytries, "23.235.32.0")
        assert any(e.get("source") == "Fastly" for e in envs)

    def test_ipv6(self, pytries):
        envs = lookup(pytries, "2a04:4e40::")
        assert any(e.get("source") == "Fastly" for e in envs)


class TestZoom:
    def test_ipv4(self, pytries):
        envs = lookup(pytries, "204.80.104.0")
        assert any("Zoom" in e.get("source", "") for e in envs)


class TestGitHub:
    def test_ipv4(self, pytries):
        envs = lookup(pytries, "192.30.252.1")
        assert any(e.get("source") == "Github" for e in envs)


class TestAtlassian:
    def test_ipv4(self, pytries):
        envs = lookup(pytries, "52.82.172.1")
        assert any(e.get("source") == "Atlassian" for e in envs)


class TestPingdom:
    def test_ipv4(self, pytries):
        envs = lookup(pytries, "43.229.84.12")
        assert any(e.get("source") == "Pingdom" for e in envs)

    def test_ipv6(self, pytries):
        envs = lookup(pytries, "2a02:6ea0:c305::4041")
        assert any(e.get("source") == "Pingdom" for e in envs)


class TestDigitalOcean:
    def test_ipv4(self, pytries):
        envs = lookup(pytries, "45.55.192.0")
        assert any(e.get("source") == "DigitalOcean" for e in envs)


class TestLinode:
    def test_ipv4(self, pytries):
        envs = lookup(pytries, "72.14.177.0")
        assert any(e.get("source") == "Linode" for e in envs)


class TestMaxCDN:
    def test_ipv4(self, pytries):
        envs = lookup(pytries, "108.168.175.204")
        assert any(e.get("source") == "MaxCDN" for e in envs)


class TestGrafana:
    def test_ipv4_1(self, pytries):
        envs = lookup(pytries, "35.227.211.64")
        assert any(e.get("source") == "Grafana" for e in envs)

    def test_ipv4_2(self, pytries):
        envs = lookup(pytries, "34.117.7.29")
        assert any(e.get("source") == "Grafana" for e in envs)


class TestOkta:
    def test_ipv4(self, pytries):
        envs = lookup(pytries, "3.33.185.234")
        assert any(e.get("source") == "Okta" for e in envs)


class TestOracle:
    def test_ipv4(self, pytries):
        envs = lookup(pytries, "129.146.0.0")
        assert any(e.get("source") == "Oracle" for e in envs)


class TestInputValidation:
    def test_missing_query_params(self):
        result = belong({}, None)
        body = json.loads(result["body"])
        assert body["error"] != ""

    def test_invalid_ip(self):
        result = belong({"queryStringParameters": {"ip": "not-an-ip"}}, None)
        assert result["statusCode"] == 400

    def test_private_ip(self):
        result = belong({"queryStringParameters": {"ip": "192.168.1.1"}}, None)
        body = json.loads(result["body"])
        assert body["data"] == "Private IP"
