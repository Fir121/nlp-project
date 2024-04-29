import streamlit as st
import grader
import jinja2
import pdfkit
#from prettytable import PrettyTable, DOUBLE_BORDER



st.header("Basic model")
question = st.text_input("Enter the question:")
ref_ans = st.text_area("Enter the reference answer:")
answer = st.text_area("Enter the answer:")


if st.button("Compute"):
    grades = grader.grader(question,ref_ans,answer)
    st.divider()
    st.write("Summary:",grades)
    '''
    parameters = list(grades.keys())
    results = list(grades.values())
    div1 = 0
    div2 = 0
    div3 = 0
    div4 = 0
    for parameter in grades.keys():
        for value in grades.values():
            #for k = accuracy
            if value in range(0,26):
                parameter_div = div1
                div1+=1
            elif value in range(26,51):
                parameter_div = div2
                div2+=1
            elif value in range(51,76):
                parameter_div = div3
                div3+=1
            elif value in range(76,101):
                parameter_div = div4
                div4+=1
    final_grade = sum(results)/100
    Remarks = (["Can do Better", "Good attempt", "Great Work"]
'''
    st.divider()

