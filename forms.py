from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets."""
    
    name = StringField("Name")
    species = StringField("Species",
                          validators=[AnyOf(values=["Dog", "Cat", "Hamster"])])
    photo_url = StringField("URL of Pet Picture",
                            validators=[Optional(), URL()])
    age = IntegerField("Age",
                      validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes")
    available = BooleanField("Is the pet available for adoption?")
    
