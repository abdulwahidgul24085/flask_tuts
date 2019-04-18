
from app import app
from flask import render_template
@app.route('/') # this is a decorator funciton
@app.route('/index')
def index():
    user = {'username': 'abdulwahidugl'}
    title = 'Home'
    posts = [
        {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
        },
        {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, title=title, posts=posts)