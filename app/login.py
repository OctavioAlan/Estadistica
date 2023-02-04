from flask import Flask, render_template, redirect, request, session
from flask_oauthlib.client import OAuth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

oauth = OAuth(app)

gmail = oauth.remote_app(
    'gmail',
    consumer_key='YOUR_GMAIL_CONSUMER_KEY',
    consumer_secret='YOUR_GMAIL_CONSUMER_SECRET',
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

facebook = oauth.remote_app(
    'facebook',
    consumer_key='YOUR_FACEBOOK_CONSUMER_KEY',
    consumer_secret='YOUR_FACEBOOK_CONSUMER_SECRET',
    request_token_params={
        'scope': 'email'
    },
    base_url='https://graph.facebook.com',
    request_token_url=None,
    access_token_method='GET',
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    provider = db.Column(db.String(20))
    provider_id = db.Column(db.String(100), unique=True)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/home')
    return render_template('index.html')

@app.route('/login/gmail')
def login_gmail():
    return gmail.authorize(callback='http://localhost:5000/login/gmail/authorized')

@app.route('/login/gmail/authorized')
def login_gmail_authorized():
    resp = gmail.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.