class Credentials:
  '''
  class that generates instances of user credentials
  '''
  credentials_list=[]
  def __init__(self,website,websiteusername,password):
    self.website = website
    self.websiteusername = websiteusername
    self.password = password
  def savecredentials(self):
    '''
    method that saves credentials object to credentials list
    '''
    Credentials.credentials_list.append(self)
  def delete_credentials(self):
    '''
    delete_credentials method removes saved credentials from credentials list
    '''
    Credentials.credentials_list.remove(self)