import streamlit as st
import pandas as pd
import numpy as np

st.title("AI Travel Expense Optimizer MVP")

# User input for travel preferences
budget = st.number_input("Enter your total budget (USD)", min_value=100, max_value=10000, value=1000)
travel_type = st.selectbox("Select travel preference", ["Luxury", "Adventure", "Local Culture"])
trip_duration = st.slider("Select number of days for the trip", 1, 30, 7)

# Display the inputs for confirmation
st.write(f"Budget: ${budget}")
st.write(f"Travel Preference: {travel_type}")
st.write(f"Trip Duration: {trip_duration} days")

# Sample data for destinations and their costs
data = {
    "Destination": ["Paris", "Bangkok", "Cape Town", "Tokyo", "New York"],
    "Type": ["Luxury", "Adventure", "Local Culture", "Luxury", "Local Culture"],
    "Cost Per Day (USD)": [200, 50, 80, 150, 180]
}

df = pd.DataFrame(data)

# Filter destinations based on user preferences
filtered_destinations = df[df["Type"] == travel_type]

# Estimate total cost for the trip
filtered_destinations["Total Cost"] = filtered_destinations["Cost Per Day (USD)"] * trip_duration

# Filter options within the user's budget
affordable_destinations = filtered_destinations[filtered_destinations["Total Cost"] <= budget]

st.write("Here are some destination options within your budget:")
st.table(affordable_destinations[["Destination", "Total Cost"]])

# Simple feedback form (future scope)
if st.button('Give Feedback'):
    st.write("Thanks for your feedback!")
