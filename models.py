from flask_login import UserMixin  # Import UserMixin from flask_login
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)  # Ensure this column is defined
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    category = db.relationship('Category', lazy=True)  # Relationship to Category
    user = db.relationship('User', lazy=True)  # Relationship to User


# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # Relationship to Transaction (without backref)
    transactions = db.relationship('Transactions', lazy=True)


# Category model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    # Relationship to Transaction (without backref)
    transactions = db.relationship('Transactions', lazy=True)


# BudgetCategory model
class BudgetCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<BudgetCategory {self.name}>'



# FinancialGoal model
class FinancialGoal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    target_amount = db.Column(db.Float, nullable=False)
    target_date = db.Column(db.DateTime, nullable=False)  # Changed to DateTime for more flexibility

    def __repr__(self):
        return f'<FinancialGoal {self.name}>'



