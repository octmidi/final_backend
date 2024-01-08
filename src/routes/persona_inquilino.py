from flask import jsonify, Blueprint, request
from models import Persona, db
 
create_persona_inquilino_bp = Blueprint('create_persona_inquilino', __name__)

@create_persona_inquilino_bp.route('/create_persona_inquilino', methods=['POST'])
def create_persona_inquilino(): 
   
   data = request.json  # Se espera que los datos lleguen en formato JSON desde el front-end

   rut = data.get('rut')  #
   id_unidad = data.get('id_unidad')
   estado = data.get('estado',True)
   email = data.get('email')
   nombre = data.get('nombre')
   id_perfil = data.get('id_perfil', 2)# Establecer el valor predeterminado de id_perfil, 2 corresponde al id de perfil para "Admin"
   contrasena = data.get('contrasena')
   tareas = data.get('tareas')
   gastos = data.get('gastos')
   
      

   nuevo_inqulino = Persona(
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
        nuevo_inqulino.tareas = tareas

   if gastos:
        # Asignar los gastos a la persona
        nuevo_inqulino.gastos = gastos

   try:
        db.session.add(nuevo_inqulino)
        db.session.commit()
        return jsonify({"message": "Persona creada exitosamente", "id": nuevo_inqulino.id}), 201
   except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear la persona", "details": str(e)}), 500
