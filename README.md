# Overview

![Last Run](https://github.com/fartbagxp/aas-cidr-ranges/actions/workflows/main.yml/badge.svg)
![master](https://img.shields.io/github/last-commit/fartbagxp/aas-cidr-ranges/master)

The goal of this project is to be able to quickly determine what Software-as-a-Service (SaaS) owns a particular IP address or range of IP addresses.

**Input**: Provided an IP address: `213.199.183.0` or an IP range in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing): 213.199.183.0/24, try to provide whether this IP address or range belongs to a SaaS provider.

**Result** : `{"error": "", "data": {"region": "", "platform": "Azure", "systemService": "", "cloud": "Public"}}`

## Requirements

For coding and running locally, the following is required:

- [Python 3.11+](https://www.python.org/downloads/)
  For deployment:

## How to run locally

1. Download the code:

   ```bash
   git clone git@github.com:fartbagxp/aas-cidr-ranges.git
   ```

1. Setup dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

1. Run the code to test it out:
   - python test.py

### Upgrading old dependencies

I'm of the opinion that third party packages should be locked down to version and updated _manually_ for production builds, which is why the requirements.txt file is locked down to version.

Python does not offer a default way of updating this file natively, so one way to work around it is to run the following to trick the `requirements.txt` file into upper versions and reinstalling the setup, and freezing a locked down dependency upon completion.

```bash
sed -i 's/[~=]=/>=/' requirements.txt
pip install --upgrade --force-reinstall -r requirements.txt
pip freeze > requirements.txt
```
