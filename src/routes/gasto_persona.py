from flask import jsonify, Blueprint, request
from models import GastoPersona, db
 
create_gasto_persona_bp = Blueprint('create_gasto_persona', __name__)

@create_gasto_persona_bp.route('/create_gasto_persona', methods=['POST'])
def create_gasto_persona():
                
    data = request.json

