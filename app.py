import streamlit as st
import grader

st.header("Basic model")
question = st.text_input("Enter the question:")
ref_ans = st.text_area("Enter the reference answer:")
answer1 = st.text_area("Enter the answer 1:")
answer2 = st.text_area("Enter the answer 2:")
answer3 = st.text_area("Enter the answer 3:")

if st.button("Compute"):
    answers = [answer1,answer2,answer3]
    grades = grader.grader(question,ref_ans,answers)
    st.divider()
    st.write("Similarity for _Answer_ 1: ",grades[0],size=30)
    st.write("Similarity for _Answer_ 2: ",grades[1],size=30)
    st.write("Similarity for _Answer_ 3: ",grades[2],size=30)
    st.divider()

