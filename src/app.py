from flask import Flask
from models import db
from routes.perfil import get_all_perfil_bp  # Asegúrate de importar el blueprint de las rutas
from routes.unidad import create_unidad_bp
from routes.tarea import create_tarea_bp
from routes.gasto import create_gasto_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:10644@localhost:5434/cuentas_claras_db'

# Inicializa el objeto db con la aplicación Flask
db.init_app(app)

# Registra las rutas después de haber importado el blueprint
app.register_blueprint(get_all_perfil_bp)
app.register_blueprint(create_unidad_bp)
app.register_blueprint(create_tarea_bp)
app.register_blueprint(create_gasto_bp)

if __name__ == '__main__':
    app.run(debug=True)


#flask db init
#flask db migrate -m "initial migration"
#flask db upgrade
