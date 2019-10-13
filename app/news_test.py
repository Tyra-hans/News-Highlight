import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news = News(1234,'This is what all the fuss is about ?','I can handle that','')