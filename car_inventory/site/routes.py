from re import template
from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_template')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@site.route('/gallery')
def gallery():
    return render_template('gallery.html')