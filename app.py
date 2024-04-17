import streamlit as st
import grader

st.header("Basic model")
question = st.text_input("Enter the question:")
ref_ans = st.text_area("Enter the reference answer:")
answer = st.text_area("Enter the answer:")


if st.button("Compute"):
    grades = grader.grader(question,ref_ans,answer)
    st.divider()
    st.write("Summary:",grades)
    st.divider()

