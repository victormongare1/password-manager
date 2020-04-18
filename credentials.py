class Credentials:
  '''
  class that generates instances of user credentials
  '''
  credentials_list=[]
  def __init__(self,website,username,password):
    self.website = website
    self.username = username
    self.password = password
  def savecredentials(self):
    '''
    method that saves credentials object to credentials list
    '''
    Credentials.credentials_list.append(self)