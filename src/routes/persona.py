from flask import jsonify, Blueprint, request
from models import Persona, db
 
create_persona_bp = Blueprint('create_persona', __name__)

@create_persona_bp.route('/create_persona', methods=['POST'])
def create_persona(): 
   
   data = request.json  # Se espera que los datos lleguen en formato JSON desde el front-end

   rut = data.get('rut')  #
   id_unidad = data.get('id_unidad')
   estado = data.get('estado')
   email = data.get('email')
   nombre = data.get('nombre')
   id_perfil = data.get('id_perfil')
   contrasena = data.get('contrasena')
   tareas = data.get('tareas')
   gastos = data.get('gastos')

  nueva_persona = Persona(
        rut = rut,
        id_unidad = id_unidad,
        estado = estado,
        email = email,
        nombre = nombre,
        id_perfil = id_perfil,
        contrasena = contrasena
    )
    
    if tareas:
        # Asignar las tareas a la persona
        nueva_persona.tareas = tareas

    if gastos:
        # Asignar los gastos a la persona
        nueva_persona.gastos = gastos

    try:
        db.session.add(nueva_persona)
        db.session.commit()
        return jsonify({"message": "Persona creada exitosamente", "id": nueva_persona.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear la persona", "details": str(e)}), 500

