from flask import Blueprint, request, render_template
import json
import requests

twitter_bp = Blueprint('twitter_bp', __name__, template_folder='templates', static_url_path='static')
t_posts = []

@twitter_bp.route('/twitter/update', methods=['POST'])
def update():
    t_posts = json.loads(request.json)
    return "200"

@twitter_bp.route('/livefeed')
def livefeed():
    for i, post in enumerate(t_posts):
        t_posts[i] = requests.get(f"publish.twitter.com/oembed?url=https://twitter.com/andypiper/status/{post.id}")
    return render_template('twitter.html', posts=t_posts)