from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    #error = None
    if request.method == 'POST':
        #when request method is POST
        # if valid_login(request.form['username'],
        #                 request.form['password']):
        #     return log_the_user_in(request.form['username'])
        # else:
        #     error = 'Invalid username/password'
        return 'LoggedIn as %s' % request.form['username']
    #when the request method is GET or invalid logins provided
    #return render_template('login.html', error=error)
    #return 'Login Page displayed at this point'
    return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

@app.route('/upload', methods=['GET', 'POST'])
#Just make sure not to forget to set the enctype="multipart/form-data" 
#attribute on your HTML form, else no file will be uploaded
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/uploads/uploadedFile.txt')
        return 'file saved'
        #If you want to use the filename of the client to store the file on the server,
        #pass it through the secure_filename() function that Werkzeug provides
        #import it ==>  from werkzeug.utils import secure_filename
        #
        #f.save('/uploads/' + secure_filename(f.filename))
    return 'no download'
    
with app.test_request_context():
    print(url_for('index'))
    print(url_for('show_user_profile', username='ck chai'))

