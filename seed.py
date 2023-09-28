from models import db, connect_db, Pet
from app import app

# Database is adopt
# Table is pets

# Create all tables

db.drop_all()
db.create_all()

# If table isn't empty, empty it.

Pet.query.delete()

# Add users
buddy = Pet(name="Buddy",
            species="Dog", 
            photo_url="https://scontent-den4-1.xx.fbcdn.net/v/t39.30808-6/376251908_18382766731006915_1429434721804169190_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=49d041&_nc_ohc=F5ufyupggvQAX8YHvUC&_nc_ht=scontent-den4-1.xx&cb_e2o_trans=t&oh=00_AfBAzA2x_LsmkKVGFm_r-4tvNAeCcQY0XXHAN-njJ6EsFA&oe=65198CEE",
            age= 13)
archie = Pet(name="Archie",
            species="Cat", 
            age= 1,
            available=False)
daisy = Pet(name="Daisy",
            species="Dog", 
            photo_url="https://scontent-den4-1.xx.fbcdn.net/v/t39.30808-6/377277469_18382766713006915_4749296638001912423_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=49d041&_nc_ohc=vHnbrPkOLEMAX_wSdCf&_nc_ht=scontent-den4-1.xx&cb_e2o_trans=t&oh=00_AfDBz0dOtx4x1wNMXJbcTv6gFfh5IGGH9FqHdwxZC-hrog&oe=651A30EF",
            age= 0)
grace = Pet(name="Grace",
            species="Hamster", 
            age= 2)
mocha = Pet(name="Mocha",
            species="Cat", 
            age= 11)


db.session.add(buddy)
db.session.add(archie)
db.session.add(daisy)
db.session.add(grace)
db.session.add(mocha)

db.session.commit()

