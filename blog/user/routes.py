
from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, session,g
from blog.user.forms import RegistraionForm, LoginForm
from blog.models import *
import os
from werkzeug.utils import secure_filename
import uuid as uuid
from blog.config import Config
from flask_bcrypt import Bcrypt
from blog.hash import Hashing



user = Blueprint('user', __name__)


@user.before_request
def before_request():
    g.email = None 
    if 'email' in session:
        g.email = session['email']
        print('g.email ____________', g.email)


@user.route('/profile', methods=['POST',  'GET'])
def profile():
    if g.email: 
        try:
            print("in try block ")
            user_detail = Users.query.filter_by(email=session['email']).first()
            
            
            if request.method == 'POST':
            
                user_name = request.form.get('user_name')
                
                full_name = request.form.get('full_name')

                about_author = request.form.get('about_author')
                file = request.files['user_pic']

                filename = secure_filename(file.filename)
                print('outside ************* ')
                if filename != '':
                    print('inside ************** ')
                    config_obj = Config()
                    image_directory = config_obj.UPLOAD_FOLDER
                    filename = str(uuid.uuid1()) +  filename
                    file.save(os.path.join(image_directory, filename))
                    user_detail.user_name = user_name
                    user_detail.full_name = full_name
                    user_detail.about_author = about_author
                    user_detail.user_pic =  filename
                    db.session.commit()
                    print('***************************  ')
                    flash("Your details uploded successfully ")
                return redirect(url_for('user.profile'))
                
        except:
            return redirect(url_for('user.log_in'))

        return render_template('profile.html', user_detail = user_detail)
    return redirect('log_in')    


# @login_required
@user.route('/dashboard')
def dashboard():
    if g.email: 
        # get_or_404 if id is not available so error occure and program break and get() is not error occuring.
        print('session["user_name"]  ', session["email"], session.get("email") )

        
        # user_detail =  Users.query.get(id)
        user_detail = Users.query.filter_by(email=session['email'])
        all_post = Post.query.order_by(Post.date_posted.desc())
        user_obj = Users()
        flash('welcome to dashboard')
        return render_template('dashboard.html', session= session['email'])
    return redirect(url_for('user.log_in'))  
          


# working !
@user.route('/', methods = ['GET', 'POST'])
@user.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
    form = RegistraionForm()
    print(form)
    success_uname,success_uemail=None,None

    if request.method == 'POST': 
        
            
        if form.validate_on_submit():
            user = Users.query.filter_by(user_name=form.username.data).first()
            email = Users.query.filter_by(email=form.email.data).first()

            if(user !=None):
                flash('User Name is already exist')
            
            if(email != None):
                flash('Email Name is already exist')

            else:
                hash_pass = Hashing()
                gen_hash_pass = hash_pass.gen_hash(form.password.data)

                user = Users(user_name=form.username.data,
                            full_name=form.full_name.data, 
                            password=gen_hash_pass,
                            email=form.email.data,)

                db.session.add(user)
                db.session.commit()
                # returnning message or redirecting to the specific page
                flash('registeration successs')
                form.username.data =''
                form.full_name.data = ''
                form.password.data = ''    
                form.email.data = ''

                return redirect(url_for('user.log_in')) 

    return render_template('registration.html', form=form, success_uname=success_uname,success_uemail=success_uemail)


@user.route('/log_in', methods=['GET', 'POST'])
def log_in():
    message = None 
    form = LoginForm()
    if request.method == 'POST':
        session.pop('email', None)
        if form.validate_on_submit():
            hash_pass = Hashing()
            
            user = Users.query.filter_by(email=form.email.data).first()
            if user: 
               
                check_hash_pass = hash_pass.check_hash(user.password,form.password.data)
                
                #user = Users.query.filter_by(email=form.email.data, password=form.password.data).first()

                if check_hash_pass: 

                    #print('user from log_in(): ',user)
                    session["email"] = form.email.data
                    #print('session["email"]  : ', session["email"] )

                    form.email, form.password = '', '' 
                    flash('login successfully!! ')
                    return redirect(url_for('user.dashboard'))
                    
                  
                else:
                    # empty the input form fields
                    form.password.data = ''    
                    form.email.data = ''

                    #return redirect('sign_up')        
                    flash('Incorrect Email ID or password !!')  

            else:
                flash('Email ID does not exit !!')  

    return render_template('login.html', form=form)                



@user.route('/log_out')
def log_out():
    session['email'] = None 
    return redirect(url_for('user.log_in'))


