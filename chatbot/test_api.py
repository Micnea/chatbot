from http import client
import discord  #this is the library that is needed to implemet the bot to discord
import random   #this library is used to randomise the answers given by the bot
import pandas_datareader as net   #this library accesses information from the pandas chain of dictionaries and I used it to get the prices for the stocks
#--------------------------------------------------------------------------
client = discord.Client()
TOKEN = "OTYxMzkxMDYxMDYwNzAyMjA4.Yk4TMg.sKXPeiQicrwgOXEGAWUVYS0qIMQ"
#--------------------------------------------------------------------------

# Functions that get called later in the program
def greetings():
    response = ['Hello!','Hey','Sup','Heyo'][random.randrange(4)]
    return response
def questions_answer():
    response = ['I am doing great','I am good','I am excellent'][random.randrange(3)]
    return response
def age_answer():
    response = ['I have lived only for a few days now','I am a couple of days old','Just a few days old'][random.randrange(3)]
    return response
def get_stock_prices(ticker):
    data = net.DataReader(ticker,"yahoo")
    return data['Close'].iloc[-1]
def doings_answer():
    response = ['I can talk to you and also I can give you the price of stocks. You just have to write !stockprice and the name in the short form of the stock!']
    return response
def byes_answer():
    response = ['Bye','See you','See you later','Good Bye','Have a nice day','Cya'][random.randrange(6)]
    return response
def unknown():
    response = ['Sorry I didn\'t understand','Can you rephrase that?','Can you rephrase please?','I didn\'t get that'][random.randrange(4)]
    return response
def jokes():
    response = ['Did you hear about the mathematician who\’s afraid of negative numbers? He\’ll stop at nothing to avoid them.','Why do we tell actors to “break a leg?”Because every play has a cast.','What do you call bears with no ears? B.','Why do French people eat snails? They don\'t like fast food!',
                'What\'s red and moves up and down? A tomato in an elevator!','What is sticky and brown? A stick!'][random.randrange(6)]
    return response
def  name_answer():
    response = ['My name is BOTis','You can call me BOTis','My name is BOTis but you can call me BOTis','Call me BOTis','I go by BOTis','You can see my name in the chat','My name is the one above'][random.randrange(6)]
    return response


#A "library" of questions and inputs the user can use that get recognised by the chat bot   

greet=['hi','hello','hey','sup','heyo','hya','greets','greetings']
question=['how are you?','are you good?','how are you doing?','how you doing?']
age=['how old are you?','are you old?','when were you created?','what is your age?']
doings = ['what can you do?','what things can you do?','what do you do?','what is your usage?','help','how can you help me?','how can you help']
byes = ['good bye','bye','cya','see you later','see you','see ya']
joke = ['can you tell me a joke?','do you know any joke?','can you tell any jokes?','what joke do you know?','what jokes do you know?','can you tell a joke?']
nameq = ['what is your name?','do you have a name?','what\'s your name?','how can I call you?','your name is?','name?','how do I call you?']


# Discord implementation for the input text in the chat to get recognised and given random answers to the question by the bot
@client.event
async def on_message(message):
    usertext = message.content.lower()
    word_list = usertext.split()
    if message.author == client.user:
        return
    if usertext in greet:
        await message.channel.send(greetings())
    elif usertext in question:
        await message.channel.send(questions_answer())
    elif usertext in age:
        await message.channel.send(age_answer())
    elif message.content.startswith('!stockprice'):
        ticker = word_list[-1]
        price = get_stock_prices(word_list[-1])
        await message.channel.send(f"Acording to Yahoo Finance the stock price of {ticker} is {price} USD")
    elif usertext in doings:
        await message.channel.send(doings_answer())
    elif usertext in byes:
        await message.channel.send(byes_answer())
    elif usertext in joke:
        await message.channel.send(jokes())
    elif usertext in nameq:
        await message.channel.send(name_answer())
    elif usertext not in greet or question or age or doings or byes or joke and not message.content.startswith('!stockprice'):
        await message.channel.send(unknown())
    
        
    


# Discord bot starting up with the key
client.run(TOKEN)
