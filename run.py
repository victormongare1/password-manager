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