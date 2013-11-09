from flask import Flask, redirect
import random

app = Flask(__name__)

@app.route('/<type>/<size>')
def random_avatar(type, size):
    hash = random.getrandbits(128)
    url = 'http://www.gravatar.com/avatar/%032x?d=%s&s=%s' % (hash, type, size)
    return redirect(url)
