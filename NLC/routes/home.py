from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__, template_folder='templates', static_url_path='static')

<<<<<<< HEAD

@home_bp.route('/home')
=======
>>>>>>> f5f0eca0a95ad16458e6736aa0ddcb4dc442fd65
@home_bp.route('/')
@home_bp.route('/home')
def home():
    return render_template('home.html',name="dude")

@home_bp.route('/attire')
def attire():
    return render_template('attire.html', title="attire")

@home_bp.route('/template')
def template():
    return render_template('layout.html', title="template")


@home_bp.route('/about')
def about():
<<<<<<< HEAD
    return render_template('about.html')
=======
    return render_template('about.html', title="about_us")

@home_bp.route('/transportation')
def transportation():
    return render_template('transportation.html', title="transportation")

@home_bp.route('/attractions')
def attractions():
    return render_template('attractions.html', title="attractions")

@home_bp.route('/maps')
def maps():
    return render_template('maps.html', title="maps")

@home_bp.route('/food')
def food():
    return render_template('food.html', title="food")
>>>>>>> f5f0eca0a95ad16458e6736aa0ddcb4dc442fd65
