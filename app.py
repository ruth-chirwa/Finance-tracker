from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Transactions, Category, BudgetCategory, FinancialGoal  # Correct the model import
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'  # Path to SQLite DB
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for sessions

# Initialize the database with the Flask app
db.init_app(app)

with app.app_context():
    db.create_all()

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User Loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home Route
@app.route('/')
def home():
    return render_template('homepage.html')

# Dashboard Route
@app.route('/dashboard')
@login_required
def dashboard():
    # Fetch transactions for the logged-in user
    transactions = Transactions.query.filter_by(user_id=current_user.id).all()

    # Calculate total income and expenses
    total_income = sum(t.amount for t in transactions if t.amount > 0)
    total_expenses = sum(t.amount for t in transactions if t.amount < 0)
    balance = total_income + total_expenses

    # Categorize transactions by category (for the pie chart)
    categories = {}
    for transaction in transactions:
        if transaction.category.name not in categories:
            categories[transaction.category.name] = 0
        categories[transaction.category.name] += transaction.amount

    # Pass data to the template
    return render_template('dashboard.html',
                           username=current_user.username,
                           total_income=total_income,
                           total_expenses=total_expenses,
                           balance=balance,
                           transactions=transactions,
                           categories=categories)

# Add Transaction Route
@app.route('/transaction', methods=['POST'])
@login_required
def transaction():
    category_id = request.form.get('category')
    amount = request.form.get('amount')
    date = request.form.get('date')

    if not category_id or not amount or not date:
        flash('All fields are required.', 'error')
        return redirect(url_for('dashboard'))

    try:
        amount = float(amount)
    except ValueError:
        flash('Amount must be a valid number.', 'error')
        return redirect(url_for('dashboard'))

    new_transaction = Transactions(user_id=current_user.id, category_id=category_id, amount=amount, date=datetime.strptime(date, '%Y-%m-%d'))
    db.session.add(new_transaction)
    db.session.commit()
    flash('Transaction added successfully!', 'success')
    return redirect(url_for('dashboard'))

# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        if not username or not email or not password or not confirm_password:
            flash('All fields are required.', 'error')
            return redirect(url_for('register'))

        # Check if passwords match
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('register'))

        # Check if the email is already registered
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email is already registered.', 'error')
            return redirect(url_for('register'))

        # Hash the password securely
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Create and save the new user
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid login credentials', 'error')

    return render_template('login.html')

@app.route('/add-transaction', methods=['GET', 'POST'])
@login_required
def add_transaction():
    if request.method == 'POST':
        description = request.form.get('description')
        amount = request.form.get('amount')
        transaction_type = request.form.get('type')
        category_id = request.form.get('category')
        date = request.form.get('date')  # Get the 'date' field from the form

        # Validate the inputs
        if not description or not amount or not category_id or not date:
            flash('All fields are required.', 'error')
            return redirect(url_for('add_transaction'))

        try:
            amount = float(amount)  # Ensure amount is a valid number
        except ValueError:
            flash('Amount must be a valid number.', 'error')
            return redirect(url_for('add_transaction'))

        try:
            category_id = int(category_id)  # Ensure category_id is an integer
        except ValueError:
            flash('Invalid category selected.', 'error')
            return redirect(url_for('add_transaction'))

        try:
            transaction_date = datetime.strptime(date, '%Y-%m-%d')  # Convert the date string to a datetime object
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'error')
            return redirect(url_for('add_transaction'))

        # Determine if it's an income or expense and adjust the amount accordingly
        if transaction_type == 'income':
            amount = abs(amount)  # Ensure income is positive
        elif transaction_type == 'expense':
            amount = -abs(amount)  # Ensure expense is negative

        # Create and add transaction to the database
        new_transaction = Transactions(
            description=description,
            amount=amount,
            category_id=category_id,
            date=transaction_date,
            user_id=current_user.id  # Assuming you're storing the user_id as well
        )
        db.session.add(new_transaction)
        db.session.commit()

        flash('Transaction added successfully!', 'success')
        return redirect(url_for('dashboard'))  # Redirect to the dashboard or another page

    # Fetch categories from the database to display in the form
    categories = Category.query.all()  # Fetch all categories from the Category table
    return render_template('add-transaction.html', categories=categories)  # Pass categories to template


# Budget Route
@app.route('/budget', methods=['GET', 'POST'])
@login_required
def budget():
    if request.method == 'POST':
        category_name = request.form['category_name']
        budget_amount = float(request.form['budget_amount'])

        # Create and add new budget category to the database
        new_category = BudgetCategory(name=category_name, amount=budget_amount)
        db.session.add(new_category)
        db.session.commit()

        flash('Budget category added successfully!', 'success')
        return redirect(url_for('budget'))  # Redirect back to the budget page

    # Fetch existing budget categories from the database to display
    budget_categories = BudgetCategory.query.all()
    return render_template('budget.html', budget_categories=budget_categories)

# Goals Route
@app.route('/goals', methods=['GET', 'POST'])
@login_required
def goals():
    if request.method == 'POST':
        goal_name = request.form['goal_name']
        goal_amount = float(request.form['goal_amount'])
        goal_date = request.form['goal_date']

        # Convert goal_date to datetime object
        goal_date = datetime.strptime(goal_date, '%Y-%m-%d')

        # Create and add new financial goal to the database
        new_goal = FinancialGoal(name=goal_name, target_amount=goal_amount, target_date=goal_date)
        db.session.add(new_goal)
        db.session.commit()

        flash('Financial goal set successfully!', 'success')
        return redirect(url_for('goals'))  # Redirect back to the goals page

    # Fetch existing goals from the database to display
    financial_goals = FinancialGoal.query.all()
    return render_template('financial-goals.html', financial_goals=financial_goals)

# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)

