from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from car_inventory.forms import UserLoginForm, UserSignupForm
from car_inventory.models import User, db, check_password_hash


auth = Blueprint('auth', __name__, template_folder = 'auth_template')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserSignupForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data
            print(email, password)

            user = User(first_name=first_name, last_name=last_name, email=email, password=password)
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
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)
            logged_user = User.query.filter(User.email == email).first()
            print(logged_user)
            if logged_user and check_password_hash(logged_user.password, password):
                print('user is verified')
                login_user(logged_user)
                flash(f'Welcome to the community of CAR SELECT, {logged_user.first_name}.', 'auth-success')
            else:
                flash('Your Email/Password is incorrect.','auth-failed')
            return redirect(url_for('site.profile'))
    except:
        raise Exception('Invalid Form Data: Please check your form.')
    return render_template('signin.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))

