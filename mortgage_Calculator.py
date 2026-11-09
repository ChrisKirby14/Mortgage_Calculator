import streamlit as st

mortgage = st.number_input("Mortgage Amount (£)", value=0.0, format="%.2f")
erc = (mortgage * st.number_input("ERC Percentage (%)", value=0.0, format="%.2f") / 100)
house_value = st.number_input("House Value (£)", value=0.0, format="%.2f")
solicitor_fee = st.number_input("Solicitor fees (£)", value=0.0, format="%.2f")
estate_agent_fee = (house_value * (st.number_input("Estate Agent Percentage Fee (%)", value=0.0, format="%.2f") + 0.002) / 100)
moving_cost = st.number_input("Moving Cost (£)", value=0.0, format="%.2f")
savings = st.number_input("Savings Amount (£)", value=0.0, format="%.2f")

total_fund = house_value

total_fund = total_fund - mortgage - erc - estate_agent_fee - solicitor_fee - moving_cost

total_fund = total_fund + savings
st.write(f"Total available: £{total_fund:,.2f}")
st.divider()

house_price = st.number_input("House Price (£)", value=0.0, format="%.2f")
if house_price <= 125000:
    stamp_duty = 0
elif house_price <= 250000:
    stamp_duty = (house_price - 125000) * 0.02
elif house_price <= 925000:
    stamp_duty = 2500 +(house_price - 250000) * 0.05
elif house_price <= 1500000:
    stamp_duty = 36250 + (house_price - 925000) * 0.1
else: # Stamp duty = 12
    stamp_duty = 93750 + (house_price - 1500000) * 0.12
st.write(f"Stamp Duty: £{stamp_duty:,.2f}")

survey = st.number_input("Surveyor Cost (£)", value=0.0, format="%.2f")

remaining_funds = total_fund - house_price - stamp_duty - solicitor_fee - survey
st.write(f"Remaining Funds: £{remaining_funds:,.2f}")