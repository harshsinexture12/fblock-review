
from flask import Flask, render_template, request , flash, redirect, url_for, session, g

#from flask_session import session

# from werkzeug  import secure_filename
from werkzeug.utils import secure_filename
import uuid as uuid
from forms import *



import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretpass'


from modules import *

app.config['UPLOAD_FOLDER'] = 'static/images/'







