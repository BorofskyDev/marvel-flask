from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'Joel'}
    posts = [
        {
            'author' : {'username' : 'John'},
            'body' : 'Come look at my Marvel heroes!',
        },
        {
            'author' : {'username' : 'Susan'},
            'body' : 'Has anyone seen the new Marvel movie yet?'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)