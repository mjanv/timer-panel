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
    session['times'] = [get_start(23, 5, 0), get_start(23, 0, 0), get_start(23, 5, 24)]
    return render_template('main.html', starts = session['times'])    

@app.route("/times", methods=['GET', 'POST'])
def times():
    print(request.method)
    session['times'] = []
    if request.method == 'POST':
        d = get_start()
        d = datetime.now().replace( hour = request.values['hours'],
                                    minute  = request.values['minuts'],
                                second  = request.values['seconds'])
        session['times'] = [d, d]  
    return render_template('times.html', times = session['times'])     

if __name__ == "__main__":
    app.secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    app.run()