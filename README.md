![CIDR update cronjob](https://github.com/fartbagxp/aas-cidr-ranges/workflows/CIDR%20update%20cronjob/badge.svg?branch=master)

# Overview

This is currently a **Work-In-Progress**.

The goal of this project is to be able to quickly determine who owns a particular IP address.

It was originally created to track "as-a-service" projects but will eventually incorporate other sources for consumption.

## Requirements

- [Python 3.8+](https://www.python.org/downloads/)
- [pyenv](https://github.com/pyenv/pyenv)
- [pipenv](https://github.com/pypa/pipenv)

## How to run

1. Download the code:  
   `git clone git@github.com:fartbagxp/aas-cidr-ranges.git`
1. Setup dependencies:  
   `pipenv shell`
1. Install dependencies:  
   `pipenv install`
1. Run the code:  
   `python main.py`
