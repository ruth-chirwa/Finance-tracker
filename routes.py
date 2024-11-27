from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app import app
from models import db, User  # Ensure these are correctly defined and imported

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        # Validate passwords match
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('signup'))

        # Check for existing user
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email is already registered', 'error')
            return redirect(url_for('signup'))

        # Hash password and create user
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)

        # Save to database
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
            db.session.rollback()

    # Render signup page on GET request
    return render_template('signup.html')
