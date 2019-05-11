from django.test import TestCase
from .models import Photographer,location,category,Image
# Create your tests here.
class PhotographerTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Photographer(first_name = 'pitz', last_name ='Peter', email ='pitz@moringaschool.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pitz,Photographer))
