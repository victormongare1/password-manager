#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
def create_user(accountname,accountpassword):
  '''
  function to create a new contact 
  '''
  newuser = User(accountname,accountpassword)
  return newuser
def create_credentials(website,username,password):
  '''
  function to create a new credentials 
  '''
  new_credentials = Credentials(website,username,password)
  return new_credentials 
def save_user(user):
    '''
    Function to save user
    '''
    user.saveuser()
def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.savecredentials()
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()
def check_existing_credentials(website):
    '''
    Function that check if a credential exists with that website and return a Boolean
    '''
    return Credentials.credentials_exists(website)
def find_user(name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_by_name(name)
def display_credentials():
    '''
    Function that returns all credentials
    '''
    return Credentials.display_credentials()