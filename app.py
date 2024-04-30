import streamlit as st

st.title("My frits Streamlit application")

st.header(" Heading of my streamlit ")

st.subheader(" Sub Heading of my streamlit ")

st.text("This is an example text")

st.success("Sucess")
st.warning("Warning")
st.info("information")
st.error("Error")

if st.checkbox("Select/unselect"):
    st.text("User selected the checkbox")
else:
    st.text("User has not selected the checkbox")

state = st.radio("What is your favorite color ?", ("Red","Green","Blue"))

if state == "Blue":
    st.success("That's my favorite color as well")

occupaction = st.selectbox("What do you do ?", ["Student","Fresher","Working Profissional"])


st.text(f"Selected option is {occupaction}")

if st.button("Example button"):
    st.error("You clicked it")


st.sidebar.header("Heading of sidebar")
st.sidebar.text("Created by Ram")