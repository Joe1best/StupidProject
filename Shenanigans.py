import numpy as np
from bs4 import BeautifulSoup
import fbchat
from getpass import getpass
from fbchat.models import *

def login_fb():
    global client
    #User gives their name
    username = str(input("Username: "))
    
    #Script asks for password
    client = fbchat.Client(username,getpass())

def send_messsage():
    
    #Name of friend who you want to send a message to 
    name = str(input("Name: ")) 
    friends = client.searchForUsers(name)  # return a list of names 
    friend = friends[0] 
    
    #Input message
    msg = str(input("Message: ")) 

    #Sends the message
    sent = client.send(Message(text = msg),thread_id=friend.uid)

def send_meme(url):
    #Name of friend who you want to send a message to 
    name = str(input("Name: ")) 
    friends = client.searchForUsers(name)  # return a list of names 
    friend = friends[0] 
    msg = str(input("What do you wanna say with your meme: "))
    #Sends the message
    sent = client.sendRemoteFiles(url,message=Message(text = msg),thread_id=friend.uid,)

url = "https://i.pinimg.com/originals/44/9d/eb/449deb701dfebad299a39e40f4d404c0.jpg"
login_fb()
send_meme(url)
client.logout()