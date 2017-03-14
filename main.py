from flask import Flask
from flask import render_template, jsonify, request

from flask import session

from datetime import datetime

import random
import string

app = Flask(__name__)

def get_start(hours, minuts, seconds):
    return [datetime.now().replace(hour = int(hours), minute = int(minuts), second = int(seconds))]  

@app.route("/")
def hello(): 
    return render_template('main.html', starts = session.get('times'))    

@app.route("/times", methods=['GET', 'POST'])
def times():
    if request.method == 'POST':
        session['times'] = [] if request.form['click'] == 'Delete All' else session.get('times', []) + get_start(request.values['hours'], request.values['minuts'], request.values['seconds'])
    return render_template('times.html', times = session.get('times'))     

if __name__ == "__main__":
    app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    app.run()
