# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

#SI206 Project3 (NLTK) Part3, Dr. Van Lent
# By Hanshen Wang, Nov 10

from TwitterAPI import TwitterAPI
import tweepy


access_token = "2473973030-PJ1R1wixU6OThS8sKZVPkXHK4v6o5KfndcFDsrj"
access_token_secret = "DM6VNbxN4XtvWPWWRJxVuHKsXLIvBirixSufWyz8OXbUE"
consumer_key = "ZPVnQkA3plpVnX8FtRrYvMem7"
consumer_secret = "xFkUw83rUbYWrT2Og6s68f5orOc0JcnpTDbRc6DGi9urbjbZVf"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

api.update_with_media("pic.jpg")