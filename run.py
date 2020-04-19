#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
import csv
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
    credentials.delete_credentials(credentials)
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
def main():
  print('''                            PASSWORD MANAGER         ''')
  print('-'*80)
  print('''                  Hey there! Welcome to password manager
                             Lets get started''')
  #print("Please enter your username :")
  #username=input()
  #print("Enter your password :")
  #password=input()
  while True:
    user={}
    status=""
    def newUser():
      print("create username")
      newlogin=input()
      if newlogin in user:
        print("username already exists")
      else:
        print("Create login password")
        newpassword=input()
        user[newlogin]=newpassword
        print("Account created")
    

    print("Are you a registered user ? y/n type q to quit")
    status=input()
      
        
    if status == "y":
      print("Enter your username")
      login=input()
      print("Enter password")
      password=input()
      if login in user and user[login]==password:
        print("login successful")
      else :
        print("wrong password or user does not exist")
        break
    elif status == "n":
      newUser()
    else  :
      print("exit")
      break

        
  
 
    print('''Use the following codes to navigate through the application
      1.Use dc to display credentials.
      2.Use cc to create credentials.
      3.Use rm to remove credentials.
      4.Use ex to exit the application''')
    short_code=input().lower()  
    if short_code=="cc": 
      print("                           NEW CREDENTIALS")
      print("-"*80)
      print("Enter website name :")
      website=input()
      print("Enter website username :")
      websiteusername=input()
      print("Enter Website password :")
      websitepassword=input()
      save_credentials(create_credentials(website,websiteusername,websitepassword))
      print('\n')
      print(f'''You have added 
      Website name :{website}
      Username :{websiteusername}
      Password :{websitepassword} to your credentials''')
      with open('account1.csv','a') as f:
        writer=csv.writer(f)
        writer.writerow([f'{website}',f'{websiteusername}',f'{websitepassword}'])
      print('\n')
    elif short_code=="dc":
      if display_credentials:
        print("These are all your usernames and credentials")
        print("\n")
        counter= 0
        for credential in display_credentials():
          counter+=1
          print(f"{counter}.{website}...{websiteusername}...{websitepassword}")
          print("\n")
      else:
        print("\n")
        print("You do not have any credentials ,type cc to add credentials")
        print("\n")
    elif short_code=="rm":
      if del_credentials:
        print("Enter website of credential you want to remove:")
        credentials=input()
        if check_existing_credentials(credentials):
          for credential in del_credentials(credentials):
            print(f"credentials for website {credentials} have been deleted")
        else:
          print("credential did not exist")
    elif short_code=="ex":
      print("You have exited from the app,bye............")
      break
    
    else:
      print("COMMAND NOT FOUND,PLEASE USE THE PROVIDED CODES")     
      
if __name__ == "__main__":
  main()