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
        self.new_news = News('this is the name','This is the title','description','https://www.youtube.com/watch?v=RN75zSpYp7M','https://i.ytimg.com/vi/RN75zSpYp7M/maxresdefault.jpg',"2019-10-13T07:04:27Z","Find out what Joanna Jedrzejczyk had to say backstage after her main event performance at UFC Tampa!\r\nSubscribe to get all the latest UFC content: http://bit.ly/2uJRzRR\r\nExperience UFC live with UFC FIGHT PASS, the digital subscription service of the UFC. Vis… [+491 chars]")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()    
