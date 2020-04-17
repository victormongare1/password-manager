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

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.newuser.firstname,"Victor")
    self.assertEqual(self.newuser.lastname,"Mongare")
    self.assertEqual(self.new_credentials.website,"Gmail")
    self.assertEqual(self.new_credentials.username,"vicmongz") 
    self.assertEqual(self.new_credentials.password,"12345678")
if __name__ == "__main__":
  unittest.main()