# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "2473973030-PJ1R1wixU6OThS8sKZVPkXHK4v6o5KfndcFDsrj"
access_token_secret = "DM6VNbxN4XtvWPWWRJxVuHKsXLIvBirixSufWyz8OXbUE"
consumer_key = "ZPVnQkA3plpVnX8FtRrYvMem7"
consumer_secret = "xFkUw83rUbYWrT2Og6s68f5orOc0JcnpTDbRc6DGi9urbjbZVf"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

count = 0
sumSubj = 0
sumPloar = 0
tweets = api.search("Trump")
for tweet in tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	count += 1
	sumSubj += analysis.subjectivity
	sumPolar = analysis.polarity
	
aveSub = sumSubj/count
avePolar = sumPolar/count
print("Average subjectivity is" + str(aveSub))
print("Average polarity is" + str(avePolar))