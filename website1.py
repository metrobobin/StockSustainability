import streamlit as st

with open('style.css') as f:
       st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
       

project_title = st.markdown(":green[Sustainability] Calculator :earth_americas:")
      

RV_title = st.text_input('Revenue Growth')

EB_title = st.text_input("EBITDA[*](https://www.bdc.ca/en/articles-tools/entrepreneur-toolkit/templates-business-guides/glossary/ebitda#:~:text=EBITDA%20is%20short%20for%20earnings,and%20ability%20to%20generate%20cash.)")

NE_title = st.text_input('Number of Employees')

Weight_title = st.text_input('Weight %')

EV_title = st.text_input('Enviornmental Score')

GoV_title = st.text_input('Government Score')

SS_title = st.text_input('Social Score')

ControS_title = st.text_input('Controversial Score')