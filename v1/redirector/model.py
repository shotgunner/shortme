from os import environ

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
if environ.get("SERVER") == "production":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:pass@{}/shortme'.format(environ.get("DB_ADDRESS"))
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(6),  nullable=False)

    def __repr__(self):
        return '<URL %r %r>' % (self.url, self.short)