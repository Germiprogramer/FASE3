from flask_sqlalchemy import SQAlchemy
from routes.contacts import contacts

db = SQAlchemy()

app.register_blueprint(contacts)
