""" THIS WEEK'S PRACTICAL

    In the next practical you will create an interactive chatbot.
    This should engage the user in interesting and intelligent conversation.
    The bot should be able to ask and answer questions.
    Try to make it as realistic and life-like as possible.

    Don't use any existing natural language processing libraries.
    It's more important to try out the features of Python to create your bot.

    Not all of the information you require is in this lecture !
    You will have to use your initiative (and a search engine ;o)

    There are a number of string functions that will be useful
         (raw_input, find, replace, split, upper, lower)

    You might like to use this list of "stop words" to help in your task:

        http://www.ranks.nl/stopwords """
        
from stop_words import get_stop_words

stop_words = get_stop_words('en')
stop_words = get_stop_words('english')

from stop_words import safe_get_stop_words

stop_words = safe_get_stop_words('unsupported language')

#Ask questions and store user input in variables

name = raw_input("What is your name?")

 #stop_words run through the user input text and pick out the name
 #print out a 'Hello'etc + username

how = raw_input("How are you?")
