from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint #importing the render template function



views = Blueprint('views', __name__)


@views.route("/")
def about():
    return render_template("about.html")