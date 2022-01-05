from flask import Flask
from werkzeug.wrappers import request
app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

import models
models.db.init_app(app)

# PART TWO
# Print all the data in the properties table.
# Print just the names of all owners.
# Print the names and ages of all owners who are older than 30.
# Look up William, save him to a variable, and print it
# Look up archstone, save it to a variable, and print it.
# Change Jane's age to 30.
# Change Jane's name to Janet.

def all_owners():
    owners = models.Owner.query.all()
    print('\n OWNER TABLE DATA \n')
    for i,owner in enumerate(owners):
        print(f'{i+1}. {owner.name}, {owner.age}')
    print('\n')
    return 'ok'
app.route('/owners', methods=['GET'])(all_owners)

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
        models.Apartment(name='Zenith Hills',units=10,owner_id=5), 
        models.Apartment(name='Willowspring',units=30,owner_id=6), 
        models.Apartment(name='Hilltop',units=200,owner_id=10)
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