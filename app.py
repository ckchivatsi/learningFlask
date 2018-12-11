from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hi')
def hi():
    return 'Hi, World!'

#Variable Rules
@app.route('/user/<username>')
def show_user_profile(username):
    #Show the user profile for that user
    return 'Welcome %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post #%d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

#Unique URLs / Redirection Behavior
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hi'))
    print(url_for('hi', next='/'))
    print(url_for('show_user_profile', username='ck chivatsi'))

