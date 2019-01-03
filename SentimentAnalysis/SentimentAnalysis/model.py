'''
Created on 19-Dec-2018

@author: Vishnu
'''

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

def Sentiment(text):
    text = text.lower()
    sid = SIA()
    ss = sid.polarity_scores(text) 
    ss.pop('compound')
    v = list(ss.values())
    k = list(ss.keys())
    maximum = k[v.index(max(v))]
    polarity_check = {'neg': 'negative', 'neu': 'neutral', 'pos': 'positive'}
    result = {}
    result['result'] = polarity_check[maximum]
    result['success'] = True
    return result
