import os
import telebot
import requests
import json
from dotenv import load_dotenv
import csv

# TODO: 1.1 Get your environment variables
load_dotenv()
yourkey = os.getenv('yourkey')
bot_id = os.getenv('bot_id')
bot = telebot.TeleBot(bot_id)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    global movielist
    movielist = []
    bot.reply_to(message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    
    # TODO: 1.2 Get movie information from the API
    name=message.text
    name=name[7:]
    response=requests.get(f"http://www.omdbapi.com/?apikey={yourkey}&t={name}")
    info=response.json()
    # print(info)
    movie_data = {
        'Title': info['Title'],
        'Year': info['Year'],
        'Released': info['Released'],
        'imdbRating': info['imdbRating']
    }
    final=[]
    for value in movie_data.values():
        final.append(value)
    movielist.append(final)
    bot.reply_to(message,'Getting movie info...')
    bot.send_message(message.chat.id,'Got movie info')
    lst2 = f"Movie name: {movie_data['Title']}\nYear: {movie_data['Year']}\nReleased: {movie_data['Released']}\nimdb Rating: {movie_data['imdbRating']}"
    bot.send_photo(message.chat.id,info['Poster'],lst2)
    header=['Title','Year','Released','imdbRating']
    
    with open('info.csv','w',encoding='UTF8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(header)
        writer.writerows(movielist)

    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    bot.send_document(message.chat.id,open('info.csv','rb'))
    #TODO: 2.2 Send downlodable CSV file to telegram chat

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
