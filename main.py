# Flask and turbo-flask
from turbo_flask import Turbo
import flask
import random
from flask import Flask, render_template, request, session
import os
from datetime import timedelta
import time
existingusers = {}


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days = 7)

# login
@app.route('/<username>', methods=['GET', 'POST'])
def home(username):
    if username in session:
        print(session.keys())
        return 'hello {}, the time is {}'.format(username, time.asctime())

    else:
        session[username] = username
        # generate this user's variable
        a[username] = 0
        print(session.keys())
        return 'login as {}'.format(username)

# logout
@app.route('/logout/<username>', methods=['GET', 'POST'])
def logout(username):
    session.pop(username)
    print(session.keys())
    return '{} logout!'.format(username)


# call add function with specific username
@app.route('/add/<username>')
def add(username):
    global a
    a[username] += 1
    return str(a[username])


if __name__ == '__main__':
    a = {}
    app.run()
    # turbo = Turbo(app)