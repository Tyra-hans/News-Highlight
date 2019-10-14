import unittest
from models import articles
Articles = articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_articles = Articles('id','author','description','https://www.youtube.com/watch?v=RN75zSpYp7M',"https://i.kinja-img.com/gawker-media/image/upload/s--yDtXY-I4--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/pj5jc9ntilzdb4dfnivl.png",'kenya','content')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))


if __name__ == '__main__':
    unittest.main()    
