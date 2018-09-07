import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test class to test behavior of the User class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_pitch = Pitch(1, 'Business', 'This is the Pitch')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))