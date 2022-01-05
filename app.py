from flask import Flask
from werkzeug.wrappers import request
app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

import models
models.db.init_app(app)

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
        id=10,
        name='Yuki',
        age=67
    )
    models.db.session.add(owner)
    models.db.session.commit()
    print('OWNER \n', owner, '\n')
    owners = models.Owner.query.all()
    print('OWNERsss \n', owners, '\n')
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
    apartments = models.Apartment.query.all()
    print('APARTMENTS \n', apartments, '\n')
    return 'ok'
app.route('/apt_test', methods=['GET'])(apt_test)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)