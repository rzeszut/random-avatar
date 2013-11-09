from flask import redirect, abort, send_file
import random
from StringIO import StringIO

from rorschach import create_rorschach_image
from random_avatar import app

@app.route('/gravatar/<type>/<size>')
def gravatar(type, size):
    hash = random.getrandbits(128)
    url = 'http://www.gravatar.com/avatar/%032x?d=%s&s=%s' % (hash, type, size)
    return redirect(url)

def serve_pil_image(im):
    im_str = StringIO()
    im.save(im_str, 'PNG')
    im_str.seek(0)
    return send_file(im_str, mimetype = 'image/png')

@app.route('/rorschach/<size>')
def rorschach(size):
    s = int(size)
    im = create_rorschach_image(s)
    return serve_pil_image(im)

