import streamlit as st 
import pandas as pd
import plotly.express as px

#----------------------------------------------------------------------
st.header('Applied Data ')
#----------------------------------------------------------------------
st.write('''
*** 
''')
#----------------------------------------------------------------------
data=pd.read_csv('.\data\Real_Estate_Sales_2001-2020_GL.csv')
#-----------------------------------------------------------------
data['Date Recorded']=pd.to_datetime(data['Date Recorded'])
data['Year'] = data['Date Recorded'].dt.year
data['Month_Name'] = data['Date Recorded'].dt.month_name()
data['Day_Name'] = data['Date Recorded'].dt.day_name()
#-----------------------------------------------------------------
data.drop(['Non Use Code','OPM remarks','Assessor Remarks','Serial Number'] ,axis=1,inplace=True)
data.drop(data.loc[data['Town']=='***Unknown***'].index, inplace=True)
data.drop(data.loc[data['Year']==1999].index, inplace=True)
data.dropna(subset=['Year'],inplace=True)
data['Year']=data['Year'].astype('int')
#------------------------------------------------------------------
from cmath import nan
data['Property Type']=data['Property Type'].replace(nan,'unknown')
data['Residential Type']=data['Residential Type'].replace(nan,'unknown')
data['Location']=data['Location'].replace(nan,'unknown')
#==================================================================
st.dataframe(data)
#==================================================================
st.header('Number Of Tales In Each Twon')
#----------------------------------------------------------------------
st.write('''
*** 
''')
#----------------------------------------------------------------------
con1=st.container()
col1,col2=con1.columns([2,5])
town=data.value_counts('Town').sort_values(ascending=False)
img1=px.bar(town,width=650,height=450)
col1.dataframe(town)
col2.plotly_chart(img1)

con2=st.container()
col1,col2=con2.columns(2)

col1.markdown('### top selling town')
col1.dataframe(town.head(10))
col2.markdown('### least selling town')
col2.dataframe(town.tail(10))
#----------------------------------------------------------------------
st.write('''
***
''')
#----------------------------------------------------------------------
st.markdown('# Sales Amount In Each Town $')

t_sales=data.groupby('Town')['Assessed Value','Sale Amount'].sum().sort_values(by='Sale Amount',ascending=False)
img2=px.bar(t_sales,barmode="group",width=900,height=600)
st.dataframe(t_sales)
st.plotly_chart(img2)

con3=st.container()
col1,col2=con3.columns(2)

img3=px.bar(t_sales.head(10),width=500,barmode='group')
col3,col4=st.columns(2)
col3.dataframe(t_sales.head(10))
col4.plotly_chart(img3)

img4=px.bar(t_sales.tail(10),width=500,barmode='group')
col5,col6=st.columns(2)
col5.dataframe(t_sales.tail(10))
col6.plotly_chart(img4)
#----------------------------------------------------------------------
st.write('''
***
''')
#----------------------------------------------------------------------
y_sales=data.groupby('Year')['Assessed Value','Sale Amount'].sum().sort_values(by='Sale Amount',ascending=False)
y_amount=data.value_counts('Year').sort_values(ascending=False)

st.markdown('# Slaes in Each Year')
#----------------------------------------------------------------------
st.write('''
***
''')
#----------------------------------------------------------------------
st.markdown('## Slaes Amount in Each Year ')
col7,col8=st.columns([1,2])
img5=px.bar(y_amount)
col7.dataframe(y_amount)
col8.plotly_chart(img5)

st.markdown('## Slaes Value in Each Year ')
col9,col10=st.columns([3,5])
img6=px.bar(y_sales,barmode='group')
col9.dataframe(y_sales)
col10.plotly_chart(img6)

year=st.selectbox('select yaer',(2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021))
if year:
   col11,col12,col13=st.columns(3)
   col11.metric('no of sales',y_amount.loc[year])
   col12.metric('Assessed Value',f"{y_sales.loc[year,'Assessed Value']} $")
   col13.metric('Sale Amount',f"{y_sales.loc[year,'Sale Amount']} $" )
   
#----------------------------------------------------------------------
st.write('''
***
''')
#----------------------------------------------------------------------
st.markdown('## Type and Number of Sold Property ')

property_type=data.value_counts('Property Type').sort_values(ascending=False)
property_type.drop(index='unknown',inplace=True)
img7=px.bar(property_type)

col14,col15=st.columns([2,5])
col14.dataframe(property_type)
col15.plotly_chart(img7)
	