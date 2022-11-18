import streamlit as st 
import pandas as pd
import numpy as npstream
import plotly.express as ex
import webbrowser

#----------------------------------------------------------------------

st.markdown(" <center>  <h1>Real Estate Sales </h1> </font> </center> </h1> ",
            unsafe_allow_html=True)
#----------------------------------------------------------------------
st.write('''
*** 
''')
#----------------------------------------------------------------------
st.markdown(''' <center>  <h5>this app is design to apply simple analysis on real estate sales with a sales price of $2,000 or greater that occur between October
 1 and September 30 of each year from 2001 to 2021</center> </h5> ''', unsafe_allow_html=True)

st.image(r".\data\real.webp", width=800)

#----------------------------------------------------------------------
st.write('''
*** 
''')
#----------------------------------------------------------------------
st.subheader('app data')
data=pd.read_csv('data\Real.csv')
st.dataframe(data)

st.subheader('for data source cilck the button')
url='https://catalog.data.gov/dataset/real-estate-sales-2001-2018'

button=st.button('click here')
if button:
    webbrowser.open_new_tab(url)
