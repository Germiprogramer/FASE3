from flask import Blueprint, render_template


contacts = Blueprint ("contact", __name__)
@contacts.route("/")
def home():
  return render_template("index.html")

@contacts.route("/new")
def add_contacto():
  return "saving a contact"

