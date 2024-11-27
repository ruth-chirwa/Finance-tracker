# Your Finance Tracker

### **Video Demo**: [Watch Here](https://youtu.be/jeYTc6mxCo8)

---

## **Overview**
Your Finance Tracker is a comprehensive, web-based personal finance and budgeting application designed to help users take control of their financial lives. Whether you're tracking daily transactions, setting up budgets, or visualizing your spending habits, this app provides the tools needed to achieve financial clarity and meet savings goals.

The application is user-friendly, highly customizable, and built to simplify personal financial management with detailed insights into income, expenses, and budgeting trends.

---

## **Tech Stack**
- **Frontend**: HTML, CSS, JavaScript (interactive elements and visualizations)
- **Backend**: Python (Flask framework for server-side logic)
- **Database**: SQLite (default) or MySQL (for advanced deployment options)
- **Visualization Library**: Chart.js (for dynamic charts and graphs)

---

## **Features**
### **1. User Authentication**
- **Secure Registration & Login**: Uses hashed passwords (`bcrypt`) to ensure security.
- Personalized dashboards provide quick access to user-specific data.

### **2. Income and Expense Management**
- **Add Transactions**: Log income or expense records with fields like:
  - **Description**: What the transaction was for.
  - **Category**: e.g., Groceries, Rent, Utilities.
  - **Amount**: The monetary value.
  - **Date**: When the transaction occurred.
- **Edit or Delete Transactions**: Easily update or remove entries.
- **Filter Options**: Search by date range, transaction type, or category.

### **3. Budgeting Tools**
- **Monthly Budgets**: Set limits for specific categories (e.g., $300 for dining out).
- Real-time budget tracking to ensure spending stays within limits.
- Alerts for overspending in any category.

### **4. Financial Goals**
- Create personalized savings goals with a:
  - Target amount.
  - Deadline for achieving the goal.
- Progress tracking visualized through percentage completion.

### **5. Transaction Categorization**
- Categorize income and expenses under user-defined or pre-set categories like:
  - Salary, Investments, Groceries, Transportation, Subscriptions, etc.
- Ability to view reports and summaries based on category.

### **6. Reports and Visualizations**
- Generate interactive charts and graphs using **Chart.js**, including:
  - **Pie Charts**: Spending breakdown by category.
  - **Bar Graphs**: Monthly income vs. expenses.
  - **Line Charts**: Trends over time for specific categories.
- Export reports to PDF or Excel (planned feature for future releases).

### **7. Recurring Transactions**
- Automate recurring entries such as:
  - Monthly rent or mortgage payments.
  - Regular subscriptions like Netflix or gym memberships.
- Avoid the hassle of repeatedly logging the same transaction.

### **8. Mobile-Friendly Design**
- Responsive layout ensures usability on desktops, tablets, and smartphones.
- Smooth navigation and optimized design for small screens.

---

## **Architecture**
### **Frontend**:
- Built with responsive and accessible HTML and CSS.
- JavaScript adds interactivity for form validation and dynamic chart updates.
- Mobile-first design ensures compatibility with all devices.

### **Backend**:
- Flask provides a lightweight, efficient web server and routes for all app functions.
- Handles data processing, user authentication, and session management.

### **Database**:
- SQLite for easy setup during development.
- Optional MySQL integration for production environments requiring scalability.

### **Visualization**:
- Charts generated dynamically with **Chart.js**, allowing users to interact with their data.

---

## **Planned Features**
- **Data Import/Export**: Import bank statements or export financial data to CSV/Excel.
- **Multi-Currency Support**: Log transactions in various currencies with live exchange rates.
- **Email Notifications**: Monthly summaries, goal progress alerts, and overspending warnings.
- **AI Insights**: Recommendations for cutting unnecessary expenses based on spending patterns.

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/ruth-chirwa/your-finance-tracker.git

2. Navigate to the Project Directory:
    ```bash
    cd your-finance-tracker

## **How to Use**
- **Sign Up**: Create an account to access the dashboard.
- **Log Transactions**: Add income and expenses with categories.
- **Set Budgets**: Define monthly spending limits.
- **Track Goals**: Monitor your savings and progress.
- **Visualize Trends**: View charts for spending analysis and financial health.

---

## **About the Developer**
- **Name**: Ruth Chirwa
- **GitHub**: [ruth-chirwa](https://github.com/ruth-chirwa)
- **edX Username**: Ruth Chirwa
- **Location**: Lilongwe, Malawi
