import unittest
from app.models import User

class UserTest(unittest.TestCase):
    '''
    Test class to test behavior of the User class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_user = User(1, 'Michel', 'michel@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))
        