from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, validators, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PostsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()] )
    post_pic = FileField('Post Pic', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit  = SubmitField('Submit',  validators=[DataRequired()])


