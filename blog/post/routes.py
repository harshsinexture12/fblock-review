from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, session,g
from blog.post.forms import PostsForm
from blog.models import *
import os
from werkzeug.utils import secure_filename
import uuid as uuid
from blog.config import Config



post = Blueprint('post', __name__)


@post.before_request
def before_request():
    g.email = None 
    if 'email' in session:
        g.email = session['email']
        print('g.email ____________', g.email)


@post.route('/show_post')
def show_my_post():
    if g.email: 
        user_data = Users.query.filter_by(email=session['email']).first()
        user_id = user_data.id 
        posts = Post.query.filter_by(user_id=user_id)  
        
        for i in  posts:
            print("post details : ",  i.file, i.content)
        return render_template('show_post.html', posts=posts, user_name=user_data.user_name)
    return redirect(url_for('user.log_in'))    

@post.route('/all_post')
def show_all_post():
    if g.email: 
        posts = Post.query.all()

        for i in posts:
            print("post details : ",  i.file, i.content)
        return render_template('show_post.html', posts=posts,Users=Users())
    return redirect(url_for('user.log_in'))    





# @post.route('/delete_post/<int:id>')
# def delete_post(id):
#     post_delete = Post.query.get_or_404(id)
#     print('User delete *********** : ', post_delete)
#     try:
#         db.session.delete(post_delete)
#         db.session.commit()
#     except:
#       flash("Error invalid user id ")
#       return 'deleted post'
#     finally:
#         return  'deleted'






@post.route('/add_post', methods= ['POST', 'GET'])
def add_post():
    print('g.email +++++++++++++ ', g.email)
    if g.email: 
        form = PostsForm()
        # user_detail =  Users.query.get(id)
        user_detail = Users.query.filter_by(email=session['email']).first()
        user_id = user_detail.id 
        if request.method == 'POST':
            print('in post ************* ')
            if form.validate_on_submit():
                config_obj = Config()
                file = request.files['post_pic']
                image_directory = config_obj.UPLOAD_FOLDER
                print("in validate_on_submit *************  ")

                filename = secure_filename(file.filename)
                
                filename = str(uuid.uuid1()) +  filename
         
                
                file.save(os.path.join(image_directory, filename))
       
                post =  Post(title=form.title.data, content=form.content.data, user_id= user_id, file=filename )
                db.session.add(post)
                db.session.commit()
                flash("successfully add post")
                return redirect(url_for('user.dashboard'))
       
            
            # form.title.data, form.content.data = '', ''

        return render_template('add_post.html', form=form, user_detail=user_detail) 
    return redirect(url_for('user.log_in'))

# @post.route("/show_data")
# def show_data(): 
#     user_data = Users.query.order_by(Users.date_added)
#     return render_template('show_data.html', user_data=user_data)

# @post.route('/update_and_delete/<int:id>')
# def update_and_delete(id):
#     return render_template('delete_and_update_user.html', id=id)


# # Update user details 

# @post.route("/update/<int:id>", methods = ["POST", "GET"])
# def update(id):
#      form = Registraion()
#      update_user =  Users.query.get_or_404(id)
#      if request.method == "POST":
#         print("get id  ********* ", update_user)
#         update_user.user_name = request.form['user_name']
#         update_user.mobile_number = request.form['mobile_number']

#         try: 
#             db.session.commit()
#             print("updaated *****")
#             flash("User updated successfully ")
#             return redirect(url_for('show_data'))


#         except:
#             flash("Error")
#             return 'this is error page'

#      return render_template('update_data.html', form=form, update_user=update_user )


# @post.route('/delete/<int:id>')
# def delete(id):
#     print('id *********** : ', id)
#     user_delete = Users.query.get_or_404(id)
#     print('User delete *********** : ', user_delete)
#     try:
#         db.session.delete(user_delete)
#         db.session.commit()
#         print('User delete ***************************  ')
#         flash("user deleted ")
#     except:
#       flash("Error invalid user id ")
#       print('Except ****************  ')
#     finally:
#         return  redirect(url_for('show_data'))



# @post.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @post.route('/username/<name>')
# def username(name):
#     return f"my name fd is this {name}"


