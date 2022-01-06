from flask import Flask
from werkzeug.wrappers import request
app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

import models
models.db.init_app(app)


### PART THREE ROUTES ###
# Associate each property with an owner:
# Archstone - belongs to Yuki
# Zenith Hills - belongs to Yuki
# Willowspring - belongs to Jane
# Print all the properties that are owned by Yuki.
# Print the count (length) of how many properties Yuki owns.
# Find Willowspring's owner and print their name.
# Change Willowspring so that is now owned by Yuki.
# Print the names of the people who own properties that have 20 units or more

def add_assoc():
    apt_to_assoc = models.Apartment.query.filter_by(name='Aspen').first()
    print('\n', apt_to_assoc, '\n')
    owner_to_assoc = models.Owner.query.filter_by(id=2).first()
    owner_to_assoc.apartments.append(apt_to_assoc)
    apt_to_assoc.owner_id = owner_to_assoc.id
    models.db.session.add(apt_to_assoc)
    models.db.session.commit()
    print('\n', owner_to_assoc, owner_to_assoc.apartments, '\n')
    return 'ok'
app.route('/add', methods=['GET'])(add_assoc)


### PART TWO ROUTES ###

def all_owners():
    owners = models.Owner.query.all()
    print('\n OWNER TABLE DATA \n')
    for i,owner in enumerate(owners):
        print(f'{i+1}. {owner.name}, {owner.age}')
        for i,apartment in enumerate(owner.apartments):
            print(f'apartment: {apartment.name}, units: {apartment.units}')
    print('\n')

    return 'ok'
app.route('/owners', methods=['GET'])(all_owners)

def owner_name():
    owners = models.Owner.query.all()
    print('\n OWNER NAMES \n')
    for i,owner in enumerate(owners):
        print(f'{i+1}. {owner.name}')
    print('\n')

    return 'ok'
app.route('/owners/names', methods=['GET'])(owner_name)

def owner_age():
    owners = models.db.session.query(models.Owner).filter(models.Owner.age > 30)
    print('\n OWNER AGES \n')
    for i,owner in enumerate(owners):
        print(f'{i+1}. {owner.age}')
    print('\n')

    return 'ok'
app.route('/owners/ages', methods=['GET'])(owner_age)

def all_properties():
    apts = models.Apartment.query.all()
    print('\n APARTMENT TABLE DATA \n')
    for i,apt in enumerate(apts):
        print(f'{i+1}. name: {apt.name}, units: {apt.units}, owner id: {apt.owner_id}')
    print('\n')

    return 'ok'
app.route('/apartments', methods=['GET'])(all_properties)

def find_one():
    owner = models.db.session.query(models.Owner).filter_by(name='William').first()
    print('\n OWNER NAME \n')
    print(f'{owner.name}')
    print('\n')

    apt = models.db.session.query(models.Apartment).filter_by(name='Archstone').first()
    print('\n APARTMENT NAME \n')
    print(f'{apt.name}')
    print('\n')

    return 'ok'
app.route('/owners/5', methods=['GET'])(find_one)

def change_one():
    owner = models.db.session.query(models.Owner).filter_by(name='Jane').first()

    owner.age = 30
    models.db.session.add(owner)
    models.db.session.commit()
    print('\n UPDATED AGE \n')
    print(f'{owner.name} is now {owner.age}')
    print('\n')

    owner.name = 'Janet'
    models.db.session.add(owner)
    models.db.session.commit()
    print('\n UPDATED NAME \n')
    print(f'Jane is now {owner.name}')
    print('\n')

    return 'ok'
app.route('/owners/6', methods=['GET'])(change_one)

### PART ONE ROUTES ###

def home_test():
    dinos = models.Dino.query.all()
    print('DINOS \n', dinos, '\n')
    print('FIRST DINO \n', models.db.session.query(models.Dino).first(), '\n')

    return 'ok'
app.route('/', methods=['GET'])(home_test)

def db_test():
    dino = models.Dino(
        id=3,
        name='Test Dino Two',
        type='Testing'
    )
    models.db.session.add(dino)
    models.db.session.commit()

    return 'ok'
app.route('/db_test', methods=['GET'])(db_test)

def make_owner():
    owner = models.Owner(
        id=11,
        name='Yuki',
        age=67
    )
    models.db.session.add(owner)
    models.db.session.commit()
    print('OWNER \n', owner, '\n')

    return 'ok'
app.route('/own_test', methods=['GET'])(make_owner)

def apt_test():
    apt = models.Apartment(
        id=2,
        name='SQL Apartments',
        units=100,
        owner_id=1
    )
    models.db.session.add(apt)
    models.db.session.commit()
    print('APARTMENT CREATE \n', apt, '\n')

    return 'ok'
app.route('/apt_test', methods=['GET'])(apt_test)

def make_apt():
    apts_to_insert = [
        models.Apartment(name='McDonald',units=100), 
        models.Apartment(name='Cowden',units=300), 
        models.Apartment(name='Aspen',units=200)
    ]
    models.db.session.bulk_save_objects(apts_to_insert)
    models.db.session.commit()
    apartments = models.Apartment.query.all()
    print('ALL APARTMENTS \n', apartments, '\n')
    
    return 'ok'
app.route('/apt', methods=['GET'])(make_apt)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)