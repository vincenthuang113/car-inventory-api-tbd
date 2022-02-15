from re import template
from flask import Blueprint, render_template
from flask_login import login_required

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

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')