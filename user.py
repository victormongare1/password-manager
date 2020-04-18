class User:
  '''
  Class that generates intances of a user
  '''
  user_list=[]
  def __init__(self,firstname,lastname):
    self.firstname = firstname
    self.lastname = lastname
  def saveuser(self):
    '''
    method that saves user object to user list
    '''
    User.user_list.append(self)
