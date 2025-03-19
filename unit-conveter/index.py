import streamlit as st

st.title("Unit Converter Tool")
st.markdown("Convert Time, Length, and Weight")
st.write("Type your data below and convert it.")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_length(category, value, unit):
    if category == "Length":
        if unit == "Kilometer to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometer":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilogram to Pounds":
            return value * 2.20462    
        elif unit == "Pounds to Kilogram":
            return value / 2.20462    

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60    
        elif unit == "Minutes to Seconds":
            return value * 60    
        elif unit == "Minutes to Hours":
            return value / 60  
        elif unit == "Hours to Minutes":
            return value * 60    
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24    


if category == "Length":
    unit = st.selectbox("Select conversion", ["Kilometer to Miles", "Miles to Kilometer"])
elif category == "Weight":
    unit = st.selectbox("Select conversion", ["Kilogram to Pounds", "Pounds to Kilogram"])
elif category == "Time":
    unit = st.selectbox("Select conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("Enter the value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_length(category, value, unit)
    if result is not None:
        st.success(f"Converted Value: {result:.2f}")
    else:
        st.error("Invalid conversion")
