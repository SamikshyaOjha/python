#app requirement
height = st.number_input("Height (m)")
weight = st. number_input("weight (kg)")
if st.button("Calculate"):
    bmi = weight / (height ** 2)
    st.write(f"your BMi:.2f")