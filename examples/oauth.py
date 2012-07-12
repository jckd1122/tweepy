import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="jQ8lLnSUe9avu4haXVBg"
consumer_secret="yLGUBdjMYPozjUHzGNUXMMCPb29T65EURLynqZYZeI"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token="225261327-6OBMmwPaBH2lD4JZgE2TRKCSZWSt36Hk529XQGAf"
access_token_secret="sgWXPBGRMvMUbADQyNqSTdCOxGrpIbqPM5jIukTapw"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print api.me().name

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's 
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
api.update_status('Updating using via Tweepy!')
