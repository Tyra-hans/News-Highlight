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
        self.new_news = News('id','This is the name','description','https://www.youtube.com/watch?v=RN75zSpYp7M','category','kenya')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()    
