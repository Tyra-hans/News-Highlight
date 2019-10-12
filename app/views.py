from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and it's data
    '''
    message = 'Hello Tyra'
    return render_template('index.html', message = message)

@app.route('/news/<int:news_source_id>')
def news_source(news_source_id):

    '''
    View news source page function that returns the news sources page and it's data
    '''
    return render_template('newssource.html', id = news_source_id)