import streamlit as st
from datetime import date
import csv
import os
import pandas as pd

st.markdown(
    "<h1 style='text-align: center; color: #2E8B57;'>💰 Expense Tracker</h1>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    expense_date = st.date_input("📅 Date", value=date.today())
    amount = st.number_input("💸 Total Amount (₹)", min_value=0.0, format="%.2f")

with col2:
    category = st.selectbox("🗂️ Type of Expense", ["Food", "Travel", "Bills", "Entertainment", "Shopping", "Other"])
    payment_method = st.selectbox("💳 Payment Method", ["Cash", "UPI", "Card", "Other"])

note = st.text_input("📝 Note")

file_path = "expenses.csv"

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Submit Expense"):
    import csv
    import os

    file_path = "expenses.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header if file is new
        if not file_exists:
            writer.writerow(["Date", "Amount", "Category", "Payment Method", "Note"])

        # Write the new data
        writer.writerow([expense_date, amount, category, payment_method, note])

    
    st.success("Expense Submitted and Saved!")
 

st.markdown("---")
st.subheader("📋 Expense History")

columns = ["Date", "Amount", "Category", "Payment Method", "Note"]

if os.path.isfile(file_path):
    expenses = pd.read_csv(file_path)
    st.dataframe(expenses)
else:
    st.info("No expenses recorded yet.")
    expenses = pd.DataFrame(columns=columns)  # 👈 safe empty fallback



st.markdown("---")
st.subheader("📈 Summary")

if not expenses.empty:
    total_spent = expenses["Amount"].sum()
    st.metric("Total Spent (₹)", f"{total_spent:,.2f}")

    
    category_summary = expenses.groupby("Category")["Amount"].sum().reset_index()
    st.bar_chart(category_summary, x="Category", y="Amount")


    
