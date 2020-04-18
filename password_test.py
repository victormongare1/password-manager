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
    self.newuser= User("VictorMongare","vic123")
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
    self.assertEqual(self.newuser.accountname,"VictorMongare")
    self.assertEqual(self.newuser.accountpassword,"vic123")
    self.assertEqual(self.new_credentials.website,"Gmail")
    self.assertEqual(self.new_credentials.websiteusername,"vicmongz") 
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
  
  def test_save_multiple_user(self):
    '''
    test_save_multiple_users to check if we can save multiple user
    objects to our user_list
    '''
    self.newuser.saveuser()
    test_user = User("Test","1234") 
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
  def test_delete_user(self):
    '''
    test_delete_user to test if we can remove a user from our user list
    '''
    self.newuser.saveuser()
    test_user = User("Test","1234r")
    test_user.saveuser()
    self.newuser.delete_user()
    self.assertEqual(len(User.user_list),1)
  def test_delete_credentials(self):
    '''
    test_delete_credentials to test if we can remove credentials from our credentials list
    '''
    self.new_credentials.savecredentials()
    test_credentials = Credentials("website","username","password")
    test_credentials.savecredentials()
    self.new_credentials.delete_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)
  def test_find_account(self):
    '''
    test to to determine whether a userinformation can be displayed
    '''
    self.newuser.saveuser()
    test_user = User("Test","1234")
    test_user.saveuser()
    found_user= User.find_by_name("Test")
    self.assertEqual(found_user.accountname,test_user.accountname)
  def test_user_exists(self):
    '''
    test to check if we can return a Boolean  if we cannot find the user.
    '''
    self.newuser.saveuser()
    test_user = User("Test","1234")
    test_user.saveuser()
    user_exists = User.user_exists("Test")
    self.assertTrue(user_exists)
  def test_user_credentials(self):
    '''
    test to check if we can return a Boolean  if we cannot find the cresdentials.
    '''
    self.new_credentials.savecredentials()
    test_credentials = Credentials("website","username","password")
    test_credentials.savecredentials()
    credentials_exists = Credentials.credentials_exists("website")
    self.assertTrue(credentials_exists)  
  def test_display_credentials(self):
    '''
    method that returns a list of all credentials saved
    '''
    self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == "__main__":
  unittest.main()