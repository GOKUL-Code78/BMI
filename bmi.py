import streamlit as st

title=st.title("BMI CALCULATER :")
header=st.header("ENTER THE INFO")
weight=st.number_input("ENTER YOUR WEIGHT IN KG")
height=st.number_input("ENTER YOUR HEIGHT IN METER")
if height==0:
  st.error("Height cannot be zero")
else:
 Square=height **2
bmi=round(weight/Square,2)
if st.button("what is my BMI"): 
 bmi
 st.success(f"your BMI is {bmi}")

 if bmi<16:
  st.warning("SEVERELY UNDERWEIGHT")

 elif 16<= bmi<=16.9:
  st.warning("MODERATLY UNDERWEIGHT ☹️") 

 elif 17<=bmi<=18.4:
  st.warning("MILDLY UNDERRWEIGHT")
 
 elif 18.5<=bmi<=24.9:
  st.success("NORAML(HEALTHY WEIGHT) 😊")
  
 elif 25<=bmi <=29.9:
  st.warning ("OVERWEIGHT")

 elif 30<=bmi<=34.9:
  st.warning("OBESE CLASS I (MODERATE)")

 elif 35 <=bmi <=39.5:
  st.warning("OBESS CLASS II (SEVERE)")

 else:
  bmi>=40
  st.warning("OBESS CLASS III (VERY SEVERE OR MORBIDLY OBESE)")