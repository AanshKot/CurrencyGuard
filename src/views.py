from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint #importing the render template function

from flask_login import login_required

from .fixer_call import fixer_call
from .fixer_call import parse_data


views = Blueprint('views', __name__)


@views.route("/")
def about():
    return render_template("about.html")

@views.route("/home",methods = ['POST','GET'])
@login_required
def home():
    if(request.method == "POST"):
        input_curr = request.form.get("in-currency")

        output_curr = request.form.get("out-currency")

        result_data = fixer_call(output_curr,input_curr)

        exchange_rate = parse_data(result_data,output_curr)

        if(exchange_rate == "error"):
            flash("Please check inputted currency codes and try again", category="error")

            
            return redirect(url_for("views.home")) 
        else:

            exchange_rate_msg = f"Currency convereted successfully:  {exchange_rate}"

            flash(exchange_rate_msg,category="success")

            return redirect(url_for("views.home")) 


            



    return render_template("home.html")