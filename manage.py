#!venv/bin/python

from flask.ext.script import Manager
from random_avatar import app

manager = Manager(app)

@manager.command
def run_debug():
    app.run(debug = True)

if __name__ == "__main__":
    manager.run()
