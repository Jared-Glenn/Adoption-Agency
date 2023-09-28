"""Adoption application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "shhhhhh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()
db.create_all()


# Home

@app.route('/')
def home():
    """Main page. Shows list of all pets on site."""

    pets = Pet.query.all()
    
    return render_template("home.html", pets=pets)


# Pet page

@app.route('/<pet_id>')
def pet_page(pet_id):
    """Pet information."""
    
    pet = Pet.query.get(pet_id)

    return render_template("pet.html", pet=pet)


# Add a pet

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Form and submission for a new pet."""
    
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()
        
        return redirect(f"/{ new_pet.id }")
    else:
        return render_template("new_pet.html", form=form)