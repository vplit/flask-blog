from flask import render_template
from app import data
from app import app

@app.route("/")
def index():
    posts = data.posts
    return render_template('index.html', page_tile='Home', posts=posts)