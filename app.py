import streamlit as st

st.set_page_config(page_title="CGPA Calculator")

st.title("🎓 CGPA Calculator")

st.write("Enter your GPA for each semester")

sem1 = st.number_input("Semester 1 GPA", 0.0, 10.0)
sem2 = st.number_input("Semester 2 GPA", 0.0, 10.0)
sem3 = st.number_input("Semester 3 GPA", 0.0, 10.0)
sem4 = st.number_input("Semester 4 GPA", 0.0, 10.0)
sem5 = st.number_input("Semester 5 GPA", 0.0, 10.0)
sem6 = st.number_input("Semester 6 GPA", 0.0, 10.0)

if st.button("Calculate CGPA"):

    cgpa = (sem1 + sem2 + sem3 + sem4 + sem5 + sem6) / 6

    st.success(f"Your CGPA is: {cgpa:.2f}")

    if cgpa >= 9:
        st.balloons()
        st.write("Excellent Performance 🌟")
    elif cgpa >= 7:
        st.write("Good Performance 👍")
    else:
        st.write("Keep Improving 💪")