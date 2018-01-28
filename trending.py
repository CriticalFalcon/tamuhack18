import tweepy
from tweepy import OAuthHandler
from flask import render_template
from pytrends.request import TrendReq

# twitter api usage

# variables
twitter_names = []
twitter_urls = []
twitter_nums = []

worldNames = []
worldUrls = []
worldNums =[]

# 
consumer_key = 'a7dkcxmjqfnagQB1TUdrkvSob'
consumer_secret = 'UmHyUIDFZd7GGmujdjuPKywVPCWsEQoEO1NRPRXw7DZVvsJT6b'
access_token = '2850727860-Hy9sUoXDGOVzVJbyRy0eFJHu4Gr2myjYMA5bYet'
access_secret = 'nSUTh5FNEweF3PcW3FcZQNdCM6Oc1Dh4Zygqo08gHz3Hk'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

response = api.trends_place(23424977)
world_response = api.trends_place(1)


#return render(request, 'index.html', {'response': response})

print (str(response))
for i in range(0,len(response[0]['trends'])):
    twitter_names.append(response[0]['trends'][i]['name'])
    twitter_urls.append(response[0]['trends'][i]['url'])
    twitter_nums.append(i)

for i in range(0,len(world_response[0]['trends'])):
    worldNames.append(world_response[0]['trends'][i]['name'])
    worldUrls.append(world_response[0]['trends'][i]['url'])
    worldNums.append(i)



# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()
# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches()

urls = []
for i in range(len(trending_searches_df)):
    url = trending_searches_df.iloc[i]['imgLinkUrl']
    head = trending_searches_df.iloc[i]['title']
    #print(url)
    if url.find('sport') >= 0:
        urls.append((url,'sport',head))
    elif url.find('entertainment') >= 0:
        urls.append((url,'entertainment',head))
    elif url.find('news') >= 0:
        urls.append((url,'news',head))
    else :
        urls.append((url,'misc',head))

from flask import Flask
app = Flask(__name__)


@app.route("/twitter")
def index():
    return render_template('twitter.html', twitter_names=twitter_names, twitter_urls=twitter_urls, twitter_nums=twitter_nums)

@app.route("/worldtwitter")
def index2():
    return render_template('worldtwitter.html', worldNames=worldNames, worldUrls=worldUrls, worldNums=worldNums)

@app.route('/')
def trendingData():
    return render_template('index.html',urls=urls,twitter_names=twitter_names, twitter_urls=twitter_urls, twitter_nums=twitter_nums)

if __name__ == '__main__':
    app.run(debug=True)
