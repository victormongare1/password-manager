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
  @classmethod
  def display_credentials(cls):
    '''
    method that returns the contact list
    '''
    return cls.credentials_list
  @classmethod
  def credentials_exists(cls,website):
    '''
    Method that checks if a credentials exists from the credentials list.
    Args:
    number: website to search if it exists
    Returns :
    Boolean: True or false depending if the credentials exists
    '''
    for credentials in cls.credentials_list:
      if credentials.website == website:
        return True

    return False