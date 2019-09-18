import numpy as np
from bs4 import BeautifulSoup
import fbchat
from getpass import getpass
from fbchat.models import *

username = str(input("Username: "))
client = fbchat.Client(username,getpass())
name = str(input("Name: ")) 
friends = client.searchForUsers(name)  # return a list of names 
friend = friends[0] 
msg = str(input("Message: ")) 
sent = client.send(Message(text = msg),thread_id=friend.uid)
