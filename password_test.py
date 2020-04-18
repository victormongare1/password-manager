import unittest
from user import User
from credentials import Credentials
class TestUser(unittest.TestCase):
  '''
  test class that defines testcases for both user and credential class behaviour
  Args:
    unittest.testcase -testcase class that helps in creating test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.newuser= User("Victor","Mongare")
    self.new_credentials= Credentials("Gmail","vicmongz","12345678")
  def tearDown(self):
    '''
    does clean up after each test case has run
    '''
    User.user_list=[]
    Credentials.credentials_list=[]
  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.newuser.firstname,"Victor")
    self.assertEqual(self.newuser.lastname,"Mongare")
    self.assertEqual(self.new_credentials.website,"Gmail")
    self.assertEqual(self.new_credentials.username,"vicmongz") 
    self.assertEqual(self.new_credentials.password,"12345678")
  def test_saveuser(self):
    '''
    testcase to determine whether a user is saved to user list
    '''
    self.newuser.saveuser()
    self.assertEqual(len(User.user_list),1)
  def test_savecredentials(self):
    '''
    testcase to determine whether  credentials is saved to credentials list
    '''
    self.new_credentials.savecredentials()
    self.assertEqual(len(Credentials.credentials_list),1)
  
  def test_save_multiple_contact(self):
    '''
    test_save_multiple_users to check if we can save multiple user
    objects to our user_list
    '''
    self.newuser.saveuser()
    test_user = User("Test","contact") 
    test_user.saveuser()
    self.assertEqual(len(User.user_list),2)
  def test_save_multiple_credentials(self):
    '''
    test_save_multiple_credentials to check if we can save multiple credentilas
    objects to our credentials_list
    '''
    self.new_credentials.savecredentials()
    test_credentials = Credentials("website","username","password") 
    test_credentials.savecredentials()
    self.assertEqual(len(Credentials.credentials_list),2)  
if __name__ == "__main__":
  unittest.main()