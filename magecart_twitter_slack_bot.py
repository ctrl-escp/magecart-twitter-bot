from datetime import datetime
from argparse import ArgumentParser
from TwitterBot.tb import TwitterBot
from slackNotifier.slack_notifier import SlackNotifier


def create_parser():
	parser = ArgumentParser(description="Magecart Twitter Bot")
	parser.add_argument("target_cid", action="store", type=str, help="The target Slack channel id.")
	parser.add_argument("slack_token", action="store", type=str, help="Bearer token for slack.")
	parser.add_argument("twitter_token", action="store", type=str, help="Bearer token for Twitter.")
	parser.add_argument("-k", "--keyword", action="extend", type=str, nargs="+", default=[],
						help="Add a keyword to search for, in addition to 'magecart'.")
	return parser


def main(args):
	keywords = ["magecart"]
	keywords.extend(args.keyword)

	tb = TwitterBot(args.twitter_token, "magecart.db")
	tbks = tb.get_latest_tweets_by_keywords(keywords, 30)
	published_counter = 0
	if tbks:
		sn = SlackNotifier(args.slack_token)
		for kw in tbks:
			for tweet in tbks[kw]:
				sn.post_message(args.target_cid, f"{tweet['text']}\n\n{tweet['url']}")
				published_counter += 1

	if published_counter:
		print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Published {published_counter} tweets.")
	else:
		print(rf"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Nothing new ¯\_(ツ)_/¯")


if __name__ == '__main__':
	main(create_parser().parse_args())
