from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint #importing the render template function

from flask_login import login_required

views = Blueprint('views', __name__)


@views.route("/")
def about():
    return render_template("about.html")

@views.route("/home")
@login_required
def home():
    return render_template("home.html")