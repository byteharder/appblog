from flask_wtf import Form
from wtforms import validators, StringField
from author.form import RegisterForm

class SetupForm(RegisterForm):
    name = StringField('Blog Title', [
            validators.Required(),
            validators.Length(min=10, max=80)
        ]
    )
    
    
