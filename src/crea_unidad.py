from flask import jsonify
from models import Unidad, db

def create_unidad(nombre_unidad):
    if not nombre_unidad:
        return jsonify({"error": "El nombre de la unidad es requerido"}), 400
    
    nueva_unidad = Unidad(nombre=nombre_unidad)

    try:
        db.session.add(nueva_unidad)
        db.session.commit()
        return jsonify({"message": "Unidad creada exitosamente", "id": nueva_unidad.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear la unidad", "details": str(e)}), 500
