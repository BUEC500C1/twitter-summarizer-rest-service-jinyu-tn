#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 17:12:06 2020

@author: jinyutian
"""


import tweepy #Installed on premises
import os
import json


#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_all_tweets(username,keyword):
    #1st:build a folder to store the images 
    folder = os.path.exists('../'+username+'/'+username+'_images')
    if not folder:                   
        os.makedirs('../'+username+'/'+username+'_images')            #makedirs 
        print ("---  Building new folder...  ---")
    else:
        print ("---  There is this folder!  ---")
    
    
    
    #authorize twitter, initialize tweepy
    if consumer_key == "" or consumer_secret == "" or access_key == "" or access_secret == "":
        list_word = []
        with open('test.json') as f:
            listword= json.load(f)
            
            for i in listword:
                list_word.append(i)
            print(list_word)
            #for line in f:
            #    list_word.append(list(line.strip('\n').split(',')))
        return list_word

        
        
    else:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
        alltweets = []
    
    #index for max_id in search
        oldest = -1

    #keep grabbing tweets until it hits 100 count (the result isn't not necessarily 100 tweets)
        while len(alltweets) < 5:
        
        #get new tweets from api search
            new_tweets = api.search(q = keyword,count = 10,max_id = str(oldest),include_entities = False)
        
        #save most recent tweets
            alltweets.extend(new_tweets)
        
        #update the id of the oldest
            oldest = new_tweets[-1].id-1
            if(not new_tweets):
                break
        #print ("...%s tweets downloaded so far" % (len(alltweets)))
        print("%s tweets downloaded in total." % (len(alltweets)))   
    
        list_word = []
    #for i in range(0,20):
    #	x.append(username+str(i)+".txt")
        x = '../'+username+'/'+username+".txt"
        f = open(x,"a+")
        for j in alltweets:
            #j = j.encode('ascii', 'ignore').decode('ascii')
            list_word.append(j.text)
            #print(j.text, "\n", file = f)	#print the first 20 tweets to txt files
        f.close()
    #for j in range(0,20):
    #f = open(x[j],"a+")
    #	print(alltweets[j].text, "\n", file = f)	#print the first 20 tweets to txt files
    #	f.close()
        return list_word

#if __name__ == '__main__':
    #get keyword from search the '#' is added in front of the word for hashtag
    #username = input('Enter your username: ')
    #keyword = input('Enter the keyword you would like to search: ')
    #get_all_tweets(username,keyword)
