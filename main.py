# Author: AmirHossein Alyian
# Date: 22/03/02

from instagrapi import *

class User:

    def __init__(self, username):
        self.username = username
        self.userid = cl.user_id_from_username(self.username)
    
    def info(self):
        '''this function wil return a complete set of information
        about the account'''

        return cl.user_info(self.userid)
    
    def get_followers(self):
        ''''''

    def get_following(self):
        ''''''
    
    def is_followers(self, username):
        '''this function figure that is given username
        following the user or not, return 1 if is
        and -1 for not following'''

        if username in self.get_followers():
            return 1
        else:
            return -1
    
    def is_following(self, username):
        '''this function figure that the user
        is following given username or not, return 1 if is
        and -1 for not following'''

        if username in self.get_following():
            return 1
        else:
            return -1



def follow(self, desired_user):
    '''this function will follow the user you like by
    getting username or its userid'''   
    '''
    if not desired_user.isnumeric():
        userid = cl.user_id_from_username(desired_user)
    else:
        userid = desired_user
    '''
    userid = desired_user
    if not userid.isnumeric():
        userid = cl.user_id_from_username(userid)

    cl.user_follow(userid)

def unfollow(self, desired_user):
    '''this function will unfollow the user you like by
    getting username or its userid'''   
    '''
    if not desired_user.isnumeric():
        userid = cl.user_id_from_username(desired_user)
    else:
        userid = desired_user
    '''
    userid = desired_user
    if not userid.isnumeric():
        userid = cl.user_id_from_username(userid)

    cl.user_unfollow(userid)



cl = Client()

USER = "amirh4lyian"
PASS = "CIV8kvub3z"
cl.login(USER, PASS)