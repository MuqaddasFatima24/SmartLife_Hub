import streamlit as st

# Custom CSS
st.markdown("""
    <style>
        .finance-section {
            background-color: #fffaf6;
            padding: 2rem;
            margin-bottom: 2rem;
            border: 1px solid #e7e2dc;
            border-radius: 16px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.03);
        }

        .finance-section h2, .finance-section h3 {
            font-family: 'Playfair Display', serif;
            color: #3a3a3a;
        }

        .stTextInput, .stNumberInput, .stDateInput, .stSelectbox {
            margin-bottom: 1.5rem;
        }

        .stButton button {
            background-color: #a67c52;
            color: white;
            font-weight: 600;
            border-radius: 10px;
            border: none;
            padding: 0.5rem 1.5rem;
            margin-top: 0.5rem;
        }

        .stButton button:hover {
            background-color: #8b6e45;
        }

        .summary-box {
            background-color: #fbf9f5;
            padding: 1rem 1.5rem;
            border-radius: 12px;
            margin-bottom: 1rem;
            font-weight: 500;
            border: 1px solid #e0ddd7;
        }

        .motivational-tip {
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
            color: #5e5e5e;
        }
    </style>
""", unsafe_allow_html=True)


class Expense:
    def __init__(self, name, category, amount, date):
        self.name = name
        self.category = category
        self.amount = amount
        self.date = date

class Income:
    def __init__(self, source, amount, date):
        self.source = source
        self.amount = amount
        self.date = date

class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        self.spent = 0

    def add_expense(self, expense):
        if expense.category == self.category:
            self.spent += expense.amount

    def remaining_budget(self):
        return self.amount - self.spent

class Debt:
    def __init__(self, name, amount, interest_rate, monthly_payment):
        self.name = name
        self.amount = amount
        self.interest_rate = interest_rate
        self.monthly_payment = monthly_payment

    def remaining_debt(self):
        months = self.amount / self.monthly_payment
        return self.amount - (self.monthly_payment * months)

class SavingsGoal:
    def __init__(self, name, target_amount, current_savings=0):
        self.name = name
        self.target_amount = target_amount
        self.current_savings = current_savings

    def add_savings(self, amount):
        self.current_savings += amount

    def remaining_amount(self):
        return self.target_amount - self.current_savings

class FinanceTracker:
    def __init__(self):
        self.expenses = []
        self.income = []
        self.budgets = []
        self.debts = []
        self.savings_goals = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def add_income(self, income):
        self.income.append(income)

    def add_budget(self, budget):
        self.budgets.append(budget)

    def add_debt(self, debt):
        self.debts.append(debt)

    def add_savings_goal(self, savings_goal):
        self.savings_goals.append(savings_goal)

    def total_expenses(self):
        return sum([expense.amount for expense in self.expenses])

    def total_income(self):
        return sum([income.amount for income in self.income])

    def total_savings(self):
        return sum([goal.current_savings for goal in self.savings_goals])


def calculate_savings_roadmap(target_amount, months):
    days_in_month = 30 
    total_days = months * days_in_month
    daily_savings = target_amount / total_days
    weekly_savings = daily_savings * 7
    monthly_savings = target_amount / months
    return daily_savings, weekly_savings, monthly_savings


def show_finance_ui(st):
    if "finance_tracker" not in st.session_state:
        st.session_state.finance_tracker = FinanceTracker()
    finance_tracker = st.session_state.finance_tracker

    st.markdown('<div class="finance-section">', unsafe_allow_html=True)
    st.subheader("➕ Add an Expense")
    expense_name = st.text_input("Expense Name")
    expense_category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])
    expense_amount = st.number_input("Amount", min_value=0.0, step=1.0, key="expense_amount")
    expense_date = st.date_input("Date")

    if st.button("Add Expense"):
        expense = Expense(expense_name, expense_category, expense_amount, expense_date)
        finance_tracker.add_expense(expense)
        st.success(f"✅ Great! You've added the expense: {expense_name} for PKR {expense_amount}. Keep going!")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="finance-section">', unsafe_allow_html=True)
    st.subheader("💵 Add an Income")
    income_source = st.text_input("Income Source")
    income_amount = st.number_input("Income Amount", min_value=0.0, step=1.0, key="income_amount")
    income_date = st.date_input("Income Date")

    if st.button("Add Income"):
        income = Income(income_source, income_amount, income_date)
        finance_tracker.add_income(income)
        st.success(f"✅ Awesome! You've added income from {income_source} for PKR {income_amount}. Great job!")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="finance-section">', unsafe_allow_html=True)
    st.subheader("🎯 Set a Savings Goal")
    savings_name = st.text_input("Savings Goal Name")
    savings_target = st.number_input("Target Amount (PKR)", min_value=0.0, step=1.0)
    savings_months = st.number_input("Target Time (Months)", min_value=1, step=1)

    if st.button("Add Savings Goal"):
        savings_goal = SavingsGoal(savings_name, savings_target)
        finance_tracker.add_savings_goal(savings_goal)
        st.success(f"🎯 Well done! You've set a goal: {savings_name} for PKR {savings_target}.")

        daily, weekly, monthly = calculate_savings_roadmap(savings_target, savings_months)

        st.markdown("#### 💡 Savings Roadmap")
        st.markdown(f'<div class="summary-box">🔹 Daily: PKR {daily:.2f}<br>🔹 Weekly: PKR {weekly:.2f}<br>🔹 Monthly: PKR {monthly:.2f}</div>', unsafe_allow_html=True)

        st.markdown("#### ✨ Motivational Tips")
        st.markdown(f"<div class='motivational-tip'>💡 Tip of the Day: Save PKR {daily:.2f} daily – maybe skip that extra coffee.</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='motivational-tip'>💡 Weekly Tip: Save PKR {weekly:.2f} – try cutting back on takeout meals.</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='motivational-tip'>💡 Monthly Tip: Save PKR {monthly:.2f} – prioritize essentials over luxuries.</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="finance-section">', unsafe_allow_html=True)
    st.subheader("📊 Financial Summary")
    st.markdown(f'<div class="summary-box">💸 Total Expenses: PKR {finance_tracker.total_expenses()}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="summary-box">💰 Total Income: PKR {finance_tracker.total_income()}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="finance-section">', unsafe_allow_html=True)
    st.subheader("📌 Savings Summary")
    for goal in finance_tracker.savings_goals:
        st.markdown(f'<div class="summary-box">Goal: <strong>{goal.name}</strong><br>Target: PKR {goal.target_amount}<br>Current: PKR {goal.current_savings}<br>Remaining: PKR {goal.remaining_amount()}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
