import email

from flask import Blueprint

from flask import Flask,render_template,url_for,redirect,request,session,jsonify,flash


from werkzeug.security import   generate_password_hash,check_password_hash

from flask_login import login_user,login_required,logout_user,current_user,user_logged_in

from . import db
#import the user class
from .models import User

auth = Blueprint("auth", __name__)


@auth.route("/login",methods = ['POST','GET'])
def login():

    if request.method == "POST":
        user_email = request.form.get('email')
        user_name = request.form.get("userName")
        password = request.form.get('password')


        user = User.query.filter_by(email=user_email).first()

        if(user):

            if check_password_hash(user.password,password):

                # can use this to say welcome user_name, in the top right corner
                name = user_name
                login_message = "Logged in successfully as ".format(name)

                flash(login_message,category="success")

                #login user
                login_user(user,remember=True)

            else: 
                flash("Incorrect email or password, Please try again!",category="error")
            
            return redirect(url_for('views.home'))#return to home page
        
        else:
            flash("Email doesn't exist",category="error")

    return render_template("login.html",user=current_user)


@auth.route('/logout')
@login_required #cannot access logout route/page unless the user is logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login')) #bring back to login page



@auth.route('/sign-up',methods=["POST","GET"])
def sign_up():
    
    if(request.method == "POST"):

        user_email = request.form.get("email")
        user_name = request.form.get("userName")
        user_password1 = request.form.get("password1")
        user_password2 = request.form.get("password2")

        user = User.query.filter_by(email=user_email).first()
        
        if(user):
            flash("email already taken",category="error")
        elif(len(user_name) < 2):
            flash("Username must be greater than 2 characters",category = "error")
        elif(user_password1 != user_password2):
            flash("Passwords do not match",category="error")
        elif(len(user_email) < 4):
            flash("Email must be greater than 4 characters",category="error")
        else:

            new_user = User(email = user_email,username = user_name, password = generate_password_hash(user_password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user,remember=True)
            
            sign_up_msg = "Welcome to Currency Guard ".format(user_name)
            flash(sign_up_msg,category="success")
            
            
            return redirect(url_for("views.home"))

    return render_template("sign_up.html",user=current_user)