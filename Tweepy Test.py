from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
twitter_client = API(auth)
twitter_user = "PatMcAfeeShow"


def get_friend_list(twitter_user):
    friend_list = []
    for friend in Cursor(twitter_client.friends, id=twitter_user).items(2):
        friend_list.append(friend)
    return friend_list


tweets = []
twitter_users = []
# twitter_users.append(None)
twitter_users.append("PatMcAfeeShow")
for i in range(2):
    print(i)
    print(twitter_users)
    for tweet in Cursor(twitter_client.user_timeline, id=twitter_users[i]).items(1):
        tweets.append(tweet)
    print("len tweets = ")
    print(len(tweets))
    print(twitter_users[i])
    for friend in twitter_client.friends(twitter_users[i]):
        twitter_users.append(friend.screen_name)


print(tweets)
for tweet in tweets:
    with open("tweets.txt", 'a') as tf:
        tf.write(str(tweet))



