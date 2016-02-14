from TwitterSearch import *
import http.client
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['@WTF']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = '17b648Q7b2APpGdOMUcE2ragd',
        consumer_secret = 'UBypiaw6epxVFm7pGe4IkaUwDMuSD6sdiffu1rVsCa58KGZib5',
        access_token = '4903721027-5jP9uDJ8wcNiVdsNqAdbc8fbJ0kpWuNyfyfLhVi',
        access_token_secret = 'JOMmPxuS6QnyrJfvt6lpHWQaRc5wgkjVu9du1WrnCYMcH'
     )

    con = http.client.HTTPConnection("text-processing.com")

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        # con.request("POST","/api/sentiment/","text=ruuun")
        # resp = con.getresponse()
        # if resp.label == 'pos':
        print( 'Positive @%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)