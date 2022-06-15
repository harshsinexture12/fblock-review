from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, validators, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
# from modules import User

class RegistraionForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    full_name = StringField('Full Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    #remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    # def validate_email(self, email):
    #     if email.data != current_user.email:
    #         user = User.query.filter_by(email=email.data).first()
    #         if user:
    #             raise ValidationError('That email is taken. Please choose a different one.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')


