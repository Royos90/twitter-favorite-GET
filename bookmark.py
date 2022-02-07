import tweepy
import json 
import pprint

pp = pprint.PrettyPrinter(indent=20)
#api keys 
api_key = ""
api_secrets = ""
access_token = ""
access_secret = ""

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
 
api = tweepy.API(auth)
 
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')


user = api.get_user(screen_name='')
twitterJsonResponse = api.get_favorites(id=,max_results=4)
#for jsonObject in listOutputOfRequest:
	#pp.pprint(jsonObject)
print(user.name)
print(user.description)
print(user.location)