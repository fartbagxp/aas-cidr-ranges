![CIDR update cronjob](https://github.com/fartbagxp/aas-cidr-ranges/workflows/CIDR%20update%20cronjob/badge.svg?branch=master)

# Overview

This is currently a **Work-In-Progress**.

The goal of this project is to be able to quickly determine what Software-as-a-Service (SaaS) owns a particular IP address or range of IP addresses.

**Input**: Provided an IP address: `213.199.183.0` or an IP range in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing): 213.199.183.0/24, try to provide whether this IP address or range belongs to a SaaS provider.

**Result** : `{"error": "", "data": {"region": "", "platform": "Azure", "systemService": "", "cloud": "Public"}}`

## Requirements

For coding and running locally, the following is required:

- [Python 3.8+](https://www.python.org/downloads/)
  For deployment:

- [Node 14+](https://nodejs.org/en/)

## How to run locally

1. Download the code:
   > git clone git@github.com:fartbagxp/aas-cidr-ranges.git
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

## Deployment

1. Install deployment dependencies:  
   `npm install`
1. Package the serverless build:  
   `npm run package`
1. Run the deployment:  
   `npm run deploy`
1. The endpoint URL will be published as part of the deployment logs.
1. Test it out!  
   `curl https://<lambda endpoint>.execute-api.<aws-datacenter>.amazonaws.com/dev/belong?ip=213.199.183.0`

   Results:  
   `{"error": "", "data": {"region": "", "platform": "Azure", "systemService": "", "cloud": "Public"}}`

## Helpful links for reading

- [Examples of Serverless deployment](https://github.com/serverless/examples)

- [Rate Limits / API Keys to Serverless](https://www.serverless.com/framework/docs/providers/aws/events/apigateway/)
