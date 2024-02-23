from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import length, EqualTo, Email , DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username = username_to_check.data).first()
        if user:
            raise ValidationError("Username already exist! please try a different username")
        
    def validate_email_address(self, email_address_to_check):
        email = User.query.filter_by(email_address = email_address_to_check.data).first()
        if email:
            raise ValidationError("Email already exist! please try a different email address")
               
        
    username = StringField(label="User Name:" , validators=[length(min=2, max=30), DataRequired()])
    email_address = StringField(label="Email Address", validators=[Email(),  DataRequired()])
    password1 = PasswordField(label="Password",  validators=[length(min=6),  DataRequired()])
    password2 = PasswordField(label="Confirm Password" , validators=[EqualTo(password1),  DataRequired()])
    submit = SubmitField(label="Create Account")