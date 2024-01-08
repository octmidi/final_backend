from flask import Flask
from flask_migrate import Migrate
from models import db  # Importa la instancia de SQLAlchemy desde el archivo models
from routes.perfil import get_all_perfil_bp  # Asegúrate de importar el blueprint de las rutas
from routes.persona_admin import create_persona_admin_bp
from routes.persona_inquilino import create_persona_inquilino_bp
from routes.unidad import create_unidad_bp
from routes.tarea import create_tarea_bp
from routes.gasto import create_gasto_bp
from routes.direccion import create_direccion_bp  # Importa el blueprint de la creación de dirección

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:10644@localhost:5434/cuentas_claras_db'
db.init_app(app)  # Inicializa el objeto db con la aplicación Flask
migrate = Migrate(app, db)

# Registra las rutas después de haber importado el blueprint
app.register_blueprint(get_all_perfil_bp)
app.register_blueprint(create_unidad_bp)
app.register_blueprint(create_persona_admin_bp)
app.register_blueprint(create_persona_inquilino_bp)
app.register_blueprint(create_tarea_bp)
app.register_blueprint(create_gasto_bp)
app.register_blueprint(create_direccion_bp)  # Utiliza el mismo nombre del blueprint que has definido en el archivo de rutas

if __name__ == '__main__':
    app.run(debug=True)




#flask db init
#flask db migrate -m "initial migration"
#flask db upgrade

