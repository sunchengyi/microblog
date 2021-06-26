from flask import jsonify
from app import db

from . import bp
from .auth import basic_auth, token_auth

@bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = basic_auth.current_user().get_token()
    db.session.commit()
    return jsonify({'token': token})

@bp.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke():
    token_auth.current_user().revoke_token()
    db.session.commit()
    return '', 204