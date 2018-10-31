from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_url_path='static')

@home_bp.route('/')
@home_bp.route('/home')
def home():
    return render_template('home.html',name="dude")

@home_bp.route('/about')
def about():
    return render_template('about.html', title="about")

@home_bp.route('/template')
def template():
    return render_template('layout.html', title="template")