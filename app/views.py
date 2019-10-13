from flask import render_template
from app import app
from .request import get_news

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and it's data
    '''
    # getting trending news
    popular_news = get_news('top-headlines')
    print(popular_news)
    
    title = 'Home - Welcome to The Know,News from any place, anytime!'
    return render_template('index.html', title = title, popular = popular_news)

@app.route('/news/<news_source_name>')
def news_source(news_source_name):

    '''
    View news source page function that returns the news sources page and it's data
    '''
    return render_template('newssource.html', name = news_source_name)