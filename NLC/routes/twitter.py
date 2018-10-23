from flask import Blueprint, request

twitter_bp = Blueprint('twitter_bp', __name__, template_folder='templates', static_url_path='static')

@twitter_bp.route('/twitter/update', methods=['POST'])
def update():
    print(request.json)
    return "200"