# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response,redirect
from django.core.context_processors import csrf
from TwitterSearch import *
import requests
import json
	
def main(request,page_number=1,flag=True):
    args={}
    args.update(csrf(request))
    return render_to_response('twitts.html',args)

def search(request):
    positive=[]
    negative =[]
    neutral = []
    query = ''
    if 'q' in request.GET and request.GET['q']:
        query = request.GET['q']

        try:
            tso = TwitterSearchOrder() # create a TwitterSearchOrder object
            tso.set_keywords([query]) # let's define all words we would like to have a look for
            tso.set_language('en') # we want to see German tweets only
            tso.set_include_entities(False) # and don't give us all those entity information

            ts = TwitterSearch(
                consumer_key = '17b648Q7b2APpGdOMUcE2ragd',
                consumer_secret = 'UBypiaw6epxVFm7pGe4IkaUwDMuSD6sdiffu1rVsCa58KGZib5',
                access_token = '4903721027-5jP9uDJ8wcNiVdsNqAdbc8fbJ0kpWuNyfyfLhVi',
                access_token_secret = 'JOMmPxuS6QnyrJfvt6lpHWQaRc5wgkjVu9du1WrnCYMcH'
            )


            i=0
            for tweet in ts.search_tweets_iterable(tso):
                if i==20:
                    break
                r = requests.post("http://text-processing.com/api/sentiment/", data={'text': tweet['text']})
                a =json.loads(r.content)
                a =a['label']
                if a == 'pos':
		    positive.append(tweet['text'])
		elif a=='neutral':
                    neutral.append(tweet['text'])
                else :
                    negative.append(tweet['text'])
                i+=1
        except TwitterSearchException as e: # take care of all those ugly errors if there are some
            print(e)
	return render_to_response('searchresult.html',{'positive': positive, 'neutral': neutral, 'negative': negative,  'query':query})



