'''
views.py
'''
from flask import Blueprint, render_template

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route('/')
def index():
    '''
    Landing Page
    '''
    return render_template('index.html')
