# Flask and turbo-flask
from turbo_flask import Turbo
import random
import threading
from flask import Flask, render_template, request, session
import os
from datetime import timedelta
import time
currentsurveys = {1, 2, 3, 4}


app = Flask(__name__)
turbo = Turbo(app)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


# login
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.context_processor
def inject_load():
    for i in range(len(currentsurveys)):
        return {'load': i}

def update_load():
    with app.app_context():
        while True:
            time.sleep(5)
            turbo.push(turbo.replace(render_template('username.html'), 'load'))


# @app.before_first_request
# def before_first_request():
#     threading.Thread(target=update_load).start()


if __name__ == '__main__':
    a = {}
    app.run(host='0.0.0.0')
    #turbo = Turbo(app)
