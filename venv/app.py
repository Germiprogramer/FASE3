from flask import Flask
from routes.contacts import contacts
from flask.sqlachemy import SQLAchemy

app = Flask(__name__)

app.config["WineQT.csv"] = "mysql://username:password@localhost/contactsdb"
app.config["WineQT.csv"] = False

SQAlchemy(app)

app.register_blueprint(contacts)