# Flask and turbo-flask
from turbo_flask import Turbo
import random
import threading
from flask import Flask, render_template, request, session
import os
from datetime import timedelta
import time
existingusers = {}


app = Flask(__name__)
turbo = Turbo(app)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


# login
@app.route('/<username>', methods=['GET', 'POST'])
def home(username):
    if username in session:
        global usernow
        usernow = username
        print(session.keys())
        # return 'hello {}, the time is {}'.format(username, time.asctime())
        return render_template('index.html')

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


@app.context_processor
def inject_load():
    global usernow
    return {'load': usernow}



def update_load():
    with app.app_context():
        while True:
            time.sleep(5)
            turbo.push(turbo.replace(render_template('username.html'), 'load'))


@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()


if __name__ == '__main__':
    a = {}
    app.run(host='0.0.0.0')
    #turbo = Turbo(app)
