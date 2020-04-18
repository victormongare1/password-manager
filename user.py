class User:
  '''
  Class that generates intances of a user
  '''
  user_list=[]
  def __init__(self,accountname,accountpassword):
    self.accountname = accountname
    self.accountpassword= accountpassword
  def saveuser(self):
    '''
    method that saves user object to user list
    '''
    User.user_list.append(self)
    
  def delete_user(self):
    '''
    delete_user method removes a saved user from user list
    '''
    User.user_list.remove(self)
  @classmethod
  def find_by_name(cls,name):
    '''
    Method that takes in a accountname and returns an account that matches that name.

    Args:
    name: name that matches account
    Returns :
    account of person that matches the name.
    '''

    for user in cls.user_list:
      if user.accountname == name:
        return user
  @classmethod
  def user_exists(cls,name):
    '''
    Method that checks if a contact exists from the contact list.
    Args:
    number: Phone number to search if it exists
    Returns :
    Boolean: True or false depending if the contact exists
    '''
    for user in cls.user_list:
      if user.accountname == name:
        return True

    return False