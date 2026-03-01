# Overview

![Last Run](https://github.com/fartbagxp/aas-cidr-ranges/actions/workflows/main.yml/badge.svg)
![master](https://img.shields.io/github/last-commit/fartbagxp/aas-cidr-ranges/master)

Given an IP address or [CIDR range](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing), this project tells you which SaaS or PaaS provider owns it.

For example, `213.199.183.0` or `213.199.183.0/24` returns:

`{"error": "", "data": {"region": "", "platform": "Azure", "systemService": "", "cloud": "Public"}}`

## Requirements

- [Python 3.13+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Run locally

1. Download the code:

   ```bash
   git clone git@github.com:fartbagxp/aas-cidr-ranges.git
   ```

1. Setup dependencies:

   ```bash
   uv sync
   ```

1. Run the code to test it out:

   ```bash
   uv run --group dev pytest tests/
   ```

## Related projects

- [lord-afred's ipranges](https://github.com/lord-alfred/ipranges) - broader IP range coverage
- [kmsec-uk's bulk IP lookup](https://github.com/kmsec-uk/bulk-ip-lookup) - uses [Team Cymru's IP ASN mapping](https://www.team-cymru.com/ip-asn-mapping)
