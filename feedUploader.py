import feedparser #parse feed
import praw # reddit
import os
from os import environ

feedlist = [
    "https://www.thenewsminute.com/kerala.xml",
    "https://www.thenewsminute.com/tamil.xml",
    "https://www.thehindu.com/news/national/kerala/feeder/default.rss",
    "https://www.thehindu.com/news/national/tamil-nadu/feeder/default.rss"
    ]

keywords = ["road","fish"]   #Only show news with these links

titles = []
links = []

for i in range(len(feedlist)):
    
    tempfeed = feedparser.parse(feedlist[i])

    for j in range(len(tempfeed.entries)):

        temptitle = tempfeed.entries[j].title
        templink = tempfeed.entries[j].link

        if("kerala" in feedlist[i]):#This is url of rss feed
            temptitle = "Kerala : " + temptitle

        if("tamil" in feedlist[i] or "tamil-nadu" in feedlist[i]):
            temptitle = "Tamil Nadu : " + temptitle

        

        for word in keywords:
            if word in temptitle:
                titles.append(temptitle)
                links.append(templink)
                break    # if title has more than one word in keywords

n=3
if (n>len(titles)):
    n=len(titles)

CLIENT_ID = environ['CLIENT_ID']
CLIENT_SECRET = environ['CLIENT_SECRET']
USER_AGENT = environ['USER_AGENT']
USERNAME = environ['USERNAME']
PASSWORD = environ['PASSWORD']

reddit = praw.Reddit(client_id = CLIENT_ID, 
                     client_secret = CLIENT_SECRET, 
                     user_agent = USER_AGENT, 
                     username = USERNAME, 
                     password = PASSWORD)


reddit.validate_on_submit = True


for i in range(n):#3 as floodsgate bot limits to 3
    #reddit.subreddit("india").submit(titles[i],url = links[i], flair_id = "8f105a84-7ea0-11e3-bba1-12313b0c91be") #The flair id is of non-political posts
    reddit.subreddit("indiameymey").submit(titles[i],url = links[i])# My personal subreddit for posting random stuff


