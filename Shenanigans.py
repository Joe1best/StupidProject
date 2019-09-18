import numpy as np
from bs4 import BeautifulSoup
import fbchat
from getpass import getpass
from fbchat.models import *

#User gives their name
username = str(input("Username: "))

#Script asks for password
client = fbchat.Client(username,getpass())

#Name of friend who you want to send a message to 
name = str(input("Name: ")) 
friends = client.searchForUsers(name)  # return a list of names 
friend = friends[0] 

#Input message
msg = str(input("Message: ")) 

#Sends the message
sent = client.send(Message(text = msg),thread_id=friend.uid)
