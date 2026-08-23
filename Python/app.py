import streamlit as st
import json
import hashlib
import uuid
from pathlib import Path

# =========================
# Data Management
# =========================

class Bank:
    DATABASE = "data.json"

    @classmethod
    def load_data(cls):
        if Path(cls.DATABASE).exists():
            try:
                with open(cls.DATABASE, "r") as f:
                    return json.load(f)
            except:
                return []
        return []

    @classmethod
    def save_data(cls, data):
        with open(cls.DATABASE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def hash_pin(pin):
        return hashlib.sha256(pin.encode()).hexdigest()

    @staticmethod
    def generate_account():
        return str(uuid.uuid4())[:12].upper()

    @classmethod
    def create_account(cls, name, age, email, pin):
        data = cls.load_data()

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": cls.hash_pin(pin),
            "account_no": cls.generate_account(),
            "balance": 0
        }

        data.append(account)
        cls.save_data(data)

        return account

    @classmethod
    def authenticate(cls, account_no, pin):
        data = cls.load_data()

        for user in data:
            if (
                user["account_no"] == account_no
                and user["pin"] == cls.hash_pin(pin)
            ):
                return user

        return None

    @classmethod
    def deposit(cls, account_no, pin, amount):
        data = cls.load_data()

        for user in data:
            if (
                user["account_no"] == account_no
                and user["pin"] == cls.hash_pin(pin)
            ):
                user["balance"] += amount
                cls.save_data(data)
                return True

        return False

    @classmethod
    def withdraw(cls, account_no, pin, amount):
        data = cls.load_data()

        for user in data:
            if (
                user["account_no"] == account_no
                and user["pin"] == cls.hash_pin(pin)
            ):
                if user["balance"] >= amount:
                    user["balance"] -= amount
                    cls.save_data(data)
                    return True

        return False

    @classmethod
    def delete_account(cls, account_no, pin):
        data = cls.load_data()

        for user in data:
            if (
                user["account_no"] == account_no
                and user["pin"] == cls.hash_pin(pin)
            ):
                data.remove(user)
                cls.save_data(data)
                return True

        return False


# =========================
# Streamlit UI
# =========================

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create Account",
        "Deposit",
        "Withdraw",
        "Show Details",
        "Delete Account"
    ]
)

# =========================
# Create Account
# =========================

if menu == "Create Account":

    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, step=1)
    email = st.text_input("Email")
    pin = st.text_input("4-Digit PIN", type="password")

    if st.button("Create Account"):

        if len(pin) != 4 or not pin.isdigit():
            st.error("PIN must be exactly 4 digits")

        elif not name or not email:
            st.error("Fill all fields")

        else:
            account = Bank.create_account(
                name,
                age,
                email,
                pin
            )

            st.success("Account Created Successfully")

            st.info(
                f"Your Account Number: {account['account_no']}"
            )

# =========================
# Deposit
# =========================

elif menu == "Deposit":

    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input(
        "Amount",
        min_value=1.0
    )

    if st.button("Deposit"):

        if Bank.deposit(acc, pin, amount):
            st.success("Amount Deposited")
        else:
            st.error("Invalid Credentials")

# =========================
# Withdraw
# =========================

elif menu == "Withdraw":

    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input(
        "Amount",
        min_value=1.0
    )

    if st.button("Withdraw"):

        if Bank.withdraw(acc, pin, amount):
            st.success("Withdrawal Successful")
        else:
            st.error(
                "Invalid Credentials or Insufficient Balance"
            )

# =========================
# Show Details
# =========================

elif menu == "Show Details":

    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("View Details"):

        user = Bank.authenticate(acc, pin)

        if user:

            st.success("Account Found")

            st.json({
                "Name": user["name"],
                "Age": user["age"],
                "Email": user["email"],
                "Account No": user["account_no"],
                "Balance": user["balance"]
            })

        else:
            st.error("Invalid Credentials")

# =========================
# Delete Account
# =========================

elif menu == "Delete Account":

    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):

        if Bank.delete_account(acc, pin):
            st.success("Account Deleted")
        else:
            st.error("Invalid Credentials")