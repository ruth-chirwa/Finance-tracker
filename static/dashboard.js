// Simulate some initial data for demonstration
const incomeData = [
    { name: 'Salary', amount: 5000 },
    { name: 'Freelance Work', amount: 1200 },
];

const expenseData = [
    { name: 'Rent', amount: 1200 },
    { name: 'Groceries', amount: 300 },
    { name: 'Utilities', amount: 150 },
];

const budgetData = [
    { category: 'Groceries', budget: 300 },
    { category: 'Entertainment', budget: 200 },
    { category: 'Transport', budget: 100 },
];

// Render Income and Expenses dynamically
function renderIncomeExpenses() {
    const incomeList = document.getElementById('income-list');
    const expenseList = document.getElementById('expense-list');

    // Clear previous data
    incomeList.innerHTML = '';
    expenseList.innerHTML = '';

    // Income
    incomeData.forEach(item => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
        li.innerHTML = `${item.name} <span class="badge badge-success">$${item.amount}</span>`;
        incomeList.appendChild(li);
    });

    // Expenses
    expenseData.forEach(item => {
        const li = document.createElement('li');
        li.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');
        li.innerHTML = `${item.name} <span class="badge badge-danger">$${item.amount}</span>`;
        expenseList.appendChild(li);
    });
}

// Budgeting alert logic (check if budget exceeds)
function checkBudget() {
    const alertBox = document.getElementById('budget-alert');
    let budgetExceeded = false;

    budgetData.forEach(item => {
        if (item.budget > 500) {
            budgetExceeded = true;
        }
    });

    if (budgetExceeded) {
        alertBox.style.display = 'block';
    } else {
        alertBox.style.display = 'none';
    }
}

// Set goals logic
document.getElementById('goal-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const goalName = document.getElementById('goal-name').value;
    const goalAmount = document.getElementById('goal-amount').value;
    const goalDate = document.getElementById('goal-date').value;

    if (goalName && goalAmount && goalDate) {
        const goalList = document.getElementById('goal-list');
        const goalItem = document.createElement('div');
        goalItem.classList.add('d-flex', 'justify-content-between', 'align-items-center', 'budget-item');
        goalItem.innerHTML = `${goalName} <span class="badge badge-primary">$${goalAmount}</span>`;
        goalList.appendChild(goalItem);

        // Clear the form after submission
        document.getElementById('goal-form').reset();
    }
});

// Recurring transactions logic
document.getElementById('recurring-transaction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const description = document.getElementById('recurring-description').value;
    const amount = document.getElementById('recurring-amount').value;
    const dueDate = document.getElementById('recurring-date').value;

    if (description && amount && dueDate) {
        const recurringList = document.getElementById('recurring-list');
        const recurringItem = document.createElement('div');
        recurringItem.classList.add('d-flex', 'justify-content-between', 'align-items-center', 'budget-item');
        recurringItem.innerHTML = `${description} <span class="badge badge-warning">$${amount}</span>`;
        recurringList.appendChild(recurringItem);

        // Clear the form after submission
        document.getElementById('recurring-transaction-form').reset();
    }
});

// Chart.js - Category Spending Pie Chart
function renderCategorySpendingChart() {
    const ctx = document.getElementById('category-spending-chart').getContext('2d');
    const categorySpendingData = {
        labels: ['Groceries', 'Rent', 'Utilities', 'Transport'],
        datasets: [{
            label: 'Spending by Category',
            data: [300, 1200, 150, 100],
            backgroundColor: ['#36a2eb', '#ff6384', '#ff9f40', '#ffcd56'],
            borderColor: ['#36a2eb', '#ff6384', '#ff9f40', '#ffcd56'],
            borderWidth: 1
        }]
    };
    const options = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function(tooltipItem) {
                        return tooltipItem.label + ': $' + tooltipItem.raw;
                    }
                }
            }
        }
    };
    new Chart(ctx, {
        type: 'pie',
        data: categorySpendingData,
        options: options
    });
}

// Initialize Dashboard
function initializeDashboard() {
    renderIncomeExpenses();
    checkBudget();
    renderCategorySpendingChart();
}

// Run when the page is ready
window.onload = initializeDashboard;
