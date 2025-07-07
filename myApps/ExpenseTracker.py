st.date_input("DATE:",value=date.today())

st.number_input("Total Amount:₹",min_value=0.0)
st.selectbox("Type of Expense:",["Food","Travel","Bills","Other"])
st.selectbox("Payment Method:",["Cash","UPI","Card"])
st.text_input("Note:")
