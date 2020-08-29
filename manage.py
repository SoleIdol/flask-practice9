#!/usr/bin/env python
from flask import render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from config import app, db

manage = Manager(app)
migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)


@app.route('/')
def index():
    return render_template('index.html', title='blog博客')


if __name__ == '__main__':
    manage.run()
