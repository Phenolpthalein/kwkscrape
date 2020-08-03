import GetOldTweets3 as got
import csv
import argparse
from os.path import expanduser

parser = argparse.ArgumentParser()
parser.add_argument('--username', required=True, help='Defines the target account for scraping, @ character is not necessary')
parser.add_argument('--count', type=int, default=1000, required=False, help='Defines the amount of tweets to be scraped from an account, defaults to 1000 tweets')
parser.add_argument('--filename', required=True, help='Defines the name of the output file, make sure to include filename; works best with csv or txt.' )
# Scrape parameters
args = parser.parse_args()
# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setUsername(args.username)\
                                        .setMaxTweets(args.count)
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
user_tweets = [[tweet.text] for tweet in tweets]
with open (expanduser('~') +'\\Desktop\\' + args.filename, 'w') as file1:
    wr = csv.writer (file1, quoting=csv.QUOTE_ALL)
    wr.writerows(user_tweets)