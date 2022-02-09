from re import template
from flask import Blueprint, render_template, request, flash, redirect, url_for

from car_inventory.forms import UserLoginForm
from car_inventory.models import User, db


auth = Blueprint('auth', __name__, template_folder = 'auth_template')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data
            print(email, password)

            user = User(first_name, last_name, email, password=password)
            db.session.add(user)
            db.session.commit()

            flash(f'{first_name} You have successfully enrolled into the CAR SELECT comunity.', 'user-created')
            return redirect(url_for('auth.signin'))

    except:
        raise Exception('Invalid Form Data: Please check your form.')
    return render_template('signup.html', form=form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    return render_template('signin.html', form=form)

