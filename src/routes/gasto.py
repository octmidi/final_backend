from flask import jsonify, Blueprint, request
from models import Gasto, db
 
create_gasto_bp = Blueprint('create_gasto', __name__)

@create_gasto_bp.route('/create_gasto', methods=['POST'])
def create_gasto():
            
    data = request.json
    id_unidad = data.get('id_unidad')
    factura= data.get('factura')
    monto_original= data.get('monto')
    descripcion = data.get('descripcion')


    if not(id_unidad and factura and monto_original and descripcion):
       return jsonify({"error": "El id de la unidad, numero de factura, monto y descripcion es requerido"}), 400     

    nuevo_gasto = Gasto(id_unidad = id_unidad,
                        factura = factura,
                        monto= monto_original,
                        descripcion = descripcion
                    )
    try:
        db.session.add(nuevo_gasto)
        db.session.commit()
        return jsonify({"message": "Gasto creado exitosamente", "id": nuevo_gasto.factura}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear Gasto", "details": str(e)}), 500   
