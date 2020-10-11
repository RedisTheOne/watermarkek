from flask import Blueprint, render_template

viewsBlueprint = Blueprint('views', __name__, url_prefix='/')

@viewsBlueprint.route('/')
def viewsIndex():
    return render_template('home.html')