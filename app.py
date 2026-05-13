import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("BMI Calculator")
st.write("This app calculates your Body Mass Index based on your height and weight.")

weight = st.number_input("Enter your weight in kilograms", min_value=1.0, step=0.5)
height = st.number_input("Enter your height in centimeters", min_value=1.0, step=0.5)

if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.subheader("Result")
    st.write(f"Your BMI is: **{bmi:.2f}**")

    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 25:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 30:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
