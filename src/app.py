from flask import Flask,jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Perfil, Unidad, Comuna, Direccion, Gasto, GastoPersona, Tarea, TareaPersona, Pais, Persona, Region, Comuna



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:10644@localhost:5434/cuentas_claras_db'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/perfiles', methods=['GET'])
# http://localhost:3245/get_all_perfil
def getAllPerfil():
    try:
        # Ejemplo de consulta a la tabla User
        perfil = Perfil.query.all()

        # Transformar los resultados a un formato deseado
        perfil_list = [{"id": perfil.id, "nombre": perfil.nombre} for perfil in perfil]

        response_body = {
            "msg": "Hello, this is your GET /user response",
            "perfil": perfil_list
        }

        return jsonify(response_body), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)

#flask db init
#flask db migrate -m "initial migration"
#flask db upgrade
