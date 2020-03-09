import tweepy
import time

api_key = "Xdaq3HoXaxqBG8ZW3HejFAUGw"
api_secret = "xvAzePVTv6QHMI9G9H1fvIDIkLRc658gJlueF1lHehhlhmTKzN"
access_token = "1230185016522571776-TEDI3Y0np8cWo3joY6vFUQDlhzyxtt"
access_secret = "Ix5bB8VepMZ04mkJE0We8lZn3znVttzoBQHOsyU3uHOmv"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

tweets = []

class MyStreamListener(tweepy.StreamListener):              #Initialise an overridden version of tweepy's StreamListener
    
    def on_status(self, status):                            # If a status is detected that meets parameters,
        tweets.append(status)                               # append it to the list of tweets we are collecting
        print("got a tweet!")

myStreamListener = MyStreamListener()
tweetStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)  #create the stream using our API + class

x=True

while x:
    tweetStream.filter(track=["twitter"])                   #set up the stream to watch for "glasgow" 
    print("tweets: ")
    time.sleep(10)

