![CIDR update cronjob](https://github.com/fartbagxp/aas-cidr-ranges/workflows/CIDR%20update%20cronjob/badge.svg?branch=master)

# Overview

This is currently a **Work-In-Progress**.

The goal of this project is to be able to quickly determine what Software-as-a-Service (SaaS) owns a particular IP address or range of IP addresses.

**Input**: Provided an IP address: `213.199.183.0` or an IP range in [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing): 213.199.183.0/24, try to provide whether this IP address or range belongs to a SaaS provider.

**Result** : `{"error": "", "data": {"region": "", "platform": "Azure", "systemService": "", "cloud": "Public"}}`

## Requirements

For coding and running locally, the following is required:

- [Python 3.8+](https://www.python.org/downloads/)
- [pyenv](https://github.com/pyenv/pyenv)
- [pipenv](https://github.com/pypa/pipenv)

For deployment:

- [Node 14+](https://nodejs.org/en/)

## How to run locally

1. Download the code:  
   `git clone git@github.com:fartbagxp/aas-cidr-ranges.git`
1. Setup dependencies:  
   `pipenv shell`
1. Install dependencies:  
   `pipenv install`
1. Run the code to test it out:  
   `python test.py`

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
