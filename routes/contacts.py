from flask import Blueprint, render_template


contacts = Blueprint ("contact", __name__)
@contacts.route("/")
def home():
  return render_template("index.html")

@contacts.route("/new")
def add_contacto():
  return "saving a contact"


@contacts.route("/update")
def update():
  return "update a contact"

@contacts.route("/delete")
def delete():
  return "delete a contact"

@contacts.route("/about")
def about():
  return render_template("index.html")