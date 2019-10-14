from flask import render_template
from app import app
from .request import get_news,get_article

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and it's data
    '''
    # getting general news sources
    general_news = get_news()
    title ='Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, new = general_news)
   

@app.route('/news/<id>')
def news_news(id):

    '''
    View news page function that returns the news details page and its data
    '''

    results = get_article(id)
    return render_template('article.html', data = results)