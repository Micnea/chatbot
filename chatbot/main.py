from os import access
import re

import requests
import json
from pprint import pprint as pp
import random





def get_response(user_input):
    split_message = re.split(r'\s+|[,.;?!-]\s*' , user_input.lower())
    response = check_all_messages(split_message)
    return response

    


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # counts the words that are in the predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty +=1
    # percentage of words recognised from the user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # checks if the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def unknown():
    response = ['Sorry I didn\'t understand',
                'Could you rephrase please?',
                'I didn\'t get that'][random.randrange(3)]
    return response
def check_all_messages(message):
    highest_probabilty_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_probabilty_list
        highest_probabilty_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # responses ************************************
    response('Hello!', ['hello','hi','hey','heyo','sup','greetings'], single_response=True)
    response('I am doing good and you?', ['how','are','you','doing'], required_words=['how'])
    response('Glad to hear',['i','am','good','fine','alright'],required_words=['i','am'])
    response('My name is CoinO', ['what','is','your','name'], required_words=['what','your','name'])
    response('I can give you information about all sorts of cryptocurrencies. You just have to type the name of the crypto or you can ask to see info about all', ['what','can','you','do'], required_words=['what','do'])
    #response(long.prices , ['what','are','the','coins','there'], required_words=['what','coins'])
    
        
    


    best_match = max(highest_probabilty_list, key=highest_probabilty_list.get)
     
    return unknown() if highest_probabilty_list[best_match] < 1 else best_match







while True:
    print('Bot: ' + get_response(input('You: ')))