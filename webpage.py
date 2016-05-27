#!/usr/bin/env python

from flask import Flask, render_template, request, redirect, url_for, session, flash
import socket
from functools import wraps

app = Flask(__name__)

def send(message, address, port):
   s = socket.socket()
   host = address
   port = port
   s.connect((host,port))
   s.send(message)
   s.close()

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method =='POST':
        device = request.form.get('device')
        status = int(request.form.get('status'))
        if device == "switch_light":
            if status == 1 :
                send("light1_on", "10.0.1.24", 23)
            else :
                send("light1_off", "10.0.1.24", 23)


    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
