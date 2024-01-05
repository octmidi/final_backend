from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:10644@localhost:5434/cuentas_claras_01'
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()

#flask db init
#flask db migrate -m "initial migration"
#flask db upgrade
