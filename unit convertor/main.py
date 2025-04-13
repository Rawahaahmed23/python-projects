import streamlit as st


st.title("Unit convertor")
st.write("Convertor time and length")


catogry= st.selectbox("chose a cateogry",["Time","length","Weight"])

      
def unit1(catogry,unit,value):
      if catogry == "length":
            if unit == "kilometer to miles": 
             return value * 0.621371
            elif unit == "miles to meter":
                 return value / 0.621371

 


if catogry =="length":
    unit = st.selectbox("select a unit",["kilometer to miles","miles to meter"])


elif catogry == "Time":
      unit = st.selectbox("Select conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

elif catogry =="Weight":
        unit = st.selectbox("Select conversion", ["Kilogram to Pounds", "Pounds to Kilogram"])


value = st.number_input("enter value",min_value=0.0,format="%.2f")


if st.button("Convert"):
     result = unit1(catogry,unit,value)
     if result is not None:
       st.success(f"converted value:{result:.2f}")
     else:
          st.error("eror")