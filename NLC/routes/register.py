from flask import Blueprint, render_template

regis_bp = Blueprint('regis_bp', __name__, template_folder='templates')

@regis_bp.route('/register')
def register():
    return render_template('register.html')