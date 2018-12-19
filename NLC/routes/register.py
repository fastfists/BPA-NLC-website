from flask import Blueprint, render_template

regis_bp = Blueprint('regis_bp', __name__, template_folder='templates', static_url_path="static")


@regis_bp.route('/register')
def register():
    return render_template('register.html')

@regis_bp.route('/login')
def login():
    return render_template('login.html')