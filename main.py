from flask import Flask
from flask import render_template, jsonify, request

from flask import session

from datetime import datetime

import jinja2


import random
import string

app = Flask(__name__)

def get_start(hours, minuts, seconds):
    start = datetime.now().replace(hour = int(hours), minute = int(minuts), second = int(seconds))
    if start > datetime.now():
        return []
    return [start]  

@app.route("/")
def hello(): 
    return render_template('main.html', starts = session.get('times'), names = session.get('names'))    

@app.route("/times", methods=['GET', 'POST'])
def times():
    if request.method == 'POST':
        session['times'] = [] if request.form['click'] == 'Delete All' else session.get('times', []) + get_start(request.values['hours'], request.values['minuts'], request.values['seconds'])
        session['names'] = [] if request.form['click'] == 'Delete All' else session.get('names', []) + [request.values['name']]
    return render_template('times.html', times = session.get('times'), names = session.get('names'))     

if __name__ == "__main__":
    env = jinja2.Environment()
    env.globals.update(zip=zip)
    app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    app.run(debug=True)
