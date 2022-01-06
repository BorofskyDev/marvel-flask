@api.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    """
    [GET] /api/users
    """
    return jsonify([u.to_dict() for u in User.query.all()])