# Magecart Twitter Bot
Collect Magecart references from twitter and send them to a Slack channel.

## Installation
>git clone git@github.com:ctrl-escp/magecart-twitter-bot.git;
>cd magecart-twitter-bot;
>git submodule update --init --recursive;
>git submodule foreach --recursive python3 -m pip install -r requirements.txt;

## Usage
```
usage: magecart_twitter_slack_bot.py [-h] [-k KEYWORD [KEYWORD ...]] target_cid slack_token twitter_token

Magecart Twitter Bot

positional arguments:
  target_cid            The target Slack channel id.
  slack_token           Bearer token for slack.
  twitter_token         Bearer token for Twitter.

optional arguments:
  -h, --help            show this help message and exit
  -k KEYWORD [KEYWORD ...], --keyword KEYWORD [KEYWORD ...]
                        Add a keyword to search for, in addition to 'magecart'.
```