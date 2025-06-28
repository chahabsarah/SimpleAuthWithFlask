from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user, current_user, login_required
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from functools import wraps

main = Blueprint('main', __name__)

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash("Username already exists", "warning")
            return redirect(url_for('main.register'))

        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_pw, role=form.role.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Login failed', 'danger')
    return render_template('login.html', form=form)

@main.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'msg': 'Missing username or password'}), 400

    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(
            identity={'username': user.username, 'role': user.role},
            expires_delta=timedelta(hours=1)
        )
        return jsonify({'access_token': access_token}), 200

    return jsonify({'msg': 'Bad username or password'}), 401

@main.route('/dashboard')
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()
    return render_template('dashboard.html', role=current_user['role'])

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
