import GetOldTweets3 as got
import argparse
from pathlib import Path
import io
namedir = str(Path.home())
#adding arguments for parameters into the command line
parser = argparse.ArgumentParser()
parser.add_argument('--username', required=True, help='Defines the target account for scraping, @ character is not necessary')
parser.add_argument('--count', type=int, default=1000, required=False, help='Defines the amount of tweets to be scraped from an account, defaults to 1000 tweets')
parser.add_argument('--filename', required=True, help='Defines the name of the output file, make sure to include filename; works best with csv or txt.' )
args = parser.parse_args()
#username = args.username
#count = args.count
#filename = args.filename
# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setUsername(args.username)\
                                        .setMaxTweets(args.count)
# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
ftweet = '\n\n'.join([tweet.text for tweet in tweets])
f = io.open(namedir + '\\Desktop\\' + args.filename,'w+', encoding='utf-8')
f.write(ftweet)
f.close()
