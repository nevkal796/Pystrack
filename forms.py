from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, Email
import random

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(max=100), Email()])
    # Email field: required, max length 100, must be valid email format
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=100)])
    # Password field: required, length between 6 and 100 characters
    submit = SubmitField('Register')
    # Submit button

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    # Email required, valid email format
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class JournalForm(FlaskForm):
    prompts = [
        'Let the noise out — this space is yours.',
        'Start typing. Don’t filter. Just flow.',
        "What’s circling in your head right now?",
        "No pressure, Just write.",
        "Breath In. Let it flow.",
        "What's one thing you want to let go of today?"
    ]
    
    curr_prompt = random.choice(prompts)
    # Pick one random prompt from the list each time the form is created

    content = TextAreaField(curr_prompt, validators=[InputRequired(), Length(min=10, max=5000)])
    # Text area with the prompt as the label, required, min 10 and max 5000 chars

    submit = SubmitField('Save Entry')
