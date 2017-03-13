from flask import Flask
from flask import render_template, jsonify, request

from flask import session

from datetime import datetime

import random
import string

app = Flask(__name__)

def get_start(hours, minuts, seconds):
    return datetime.now().replace(hour = int(hours), minute = int(minuts), second = int(seconds))  

@app.route("/")
def hello(): 
    return render_template('main.html', starts = session.get('times'))    

@app.route("/times", methods=['GET', 'POST'])
def times():
    if not session.get('times'):
        session['times'] = []
    if request.method == 'POST':
        if request.form['click'] == 'Submit':
            d = get_start(request.values['hours'], request.values['minuts'], request.values['seconds'])
            session['times'] = session['times'] + [d]
        else:
            session['times'] = [] 
    return render_template('times.html', times = session['times'])     

if __name__ == "__main__":
    app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    app.run()
