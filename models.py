"""Models for Adopt."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    """Pet model."""
    
    __tablename__= "pets"
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(100),
                     nullable=False)
    species = db.Column(db.String(100),
                     nullable=False)
    photo_url = db.Column(db.String(500))
    age = db.Column(db.Integer)
    notes = db.Column(db.String(2000))
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
    
    def __repr__(self):
        """Show info about the pet."""
        
        p = self
        return f"<Pet {p.id} {p.name} {p.species} {p.photo_url} {p.age} {p.notes} {p.available}>"

