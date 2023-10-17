import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="CricStats", page_icon="🏏")

st.title("Team Stats - Batting")
st.subheader("Developed by Manan Sharma")

tab1, tab2, tab3 = st.tabs(["Tests", "ODIs","T20is"])

with tab1:   

    st.title("Men - Test Matches")

    country = "England"

    column1, column2 = st.columns([1,1], gap="small")

    df = pd.read_csv('./pages/dataset/Men Test Team Batting Stats.csv')

    with column1:
        country = st.selectbox("Country", df['Country'], key="Test")
        file = './pages/flags/' + country + '.webp'
        st.image(file)
        st.header(country)

    with column2:
        file = './pages/boards/' + country + '.webp'
        image = Image.open(file)
        st.image(image, use_column_width=True)

    country_df = df.loc[df['Country']==country]

    country_df = country_df.drop(['Country'], axis=1)

    columns = country_df.columns

    column1, column2, column3, column4  = st.columns(4, gap='small')

    with column1:
        st.metric(columns[0], country_df.get(columns[0]), delta_color="off")

    with column2:
        st.metric(columns[1], country_df.get(columns[1]), delta_color="off")

    with column3:
        st.metric(columns[2], country_df.get(columns[2]), delta_color="off")    

    with column4:
        st.metric(columns[3], country_df.get(columns[3]), delta_color="off")

    column1, column2, column3, column4  = st.columns(4, gap='small')    

    with column1:
        st.metric(columns[4], country_df.get(columns[4]), delta_color="off")

    with column2:
        st.metric(columns[5], country_df.get(columns[5]), delta_color="off")

    with column3:
        st.metric(columns[9], country_df.get(columns[9]), delta_color="off")    

    with column4:
        st.metric(columns[10], country_df.get(columns[10]), delta_color="off")

    column1, column2, column3  = st.columns([1, 1, 2], gap='small')    

    with column1:
        st.metric(columns[7], country_df.get(columns[7]), delta_color="off")

    with column2:
        st.metric(columns[8], country_df.get(columns[8]), delta_color="off")

    with column3:
        st.metric(columns[6], country_df.get(columns[6]), delta_color="off")    

    pie_values = [country_df.get(columns[1]).iat[0],country_df.get(columns[2]).iat[0],country_df.get(columns[3]).iat[0],country_df.get(columns[4]).iat[0]]

    pie_labels = [columns[1],columns[2],columns[3],columns[4]]

    fig = px.pie(country_df, values=pie_values, names=pie_labels, hole=0.33)
    st.plotly_chart(fig, use_container_width=True)

with tab2:

    st.title("Men - ODI Matches")

    country = "England"

    column1, column2 = st.columns([1,1], gap="small")

    df = pd.read_csv('./pages/dataset/Men ODI Team Batting Stats.csv')

    with column1:
        country = st.selectbox("Country", df['Country'], key = "ODI")
        file = './pages/flags/' + country + '.webp'
        st.image(file)
        st.header(country)

    with column2:
        file = './pages/boards/' + country + '.webp'
        image = Image.open(file)
        st.image(image, use_column_width=True)

    country_df = df.loc[df['Country']==country]

    country_df = country_df.drop(['Country'], axis=1)

    columns = country_df.columns

    column1, column2, column3, column4  = st.columns(4, gap='small')

    with column1:
        st.metric(columns[0], country_df.get(columns[0]), delta_color="off")

    with column2:
        st.metric(columns[1], country_df.get(columns[1]), delta_color="off")

    with column3:
        st.metric(columns[2], country_df.get(columns[2]), delta_color="off")    

    with column4:
        st.metric(columns[3], country_df.get(columns[3]), delta_color="off")

    column1, column2, column3, column4  = st.columns(4, gap='small')    

    with column1:
        st.metric(columns[4], country_df.get(columns[4]), delta_color="off")

    with column2:
        st.metric(columns[5], country_df.get(columns[5]), delta_color="off")

    with column3:
        st.metric(columns[9], country_df.get(columns[9]), delta_color="off")    

    with column4:
        st.metric(columns[10], country_df.get(columns[10]), delta_color="off")

    column1, column2, column3  = st.columns([1, 1, 2], gap='small')    

    with column1:
        st.metric(columns[7], country_df.get(columns[7]), delta_color="off")

    with column2:
        st.metric(columns[8], country_df.get(columns[8]), delta_color="off")

    with column3:
        st.metric(columns[6], country_df.get(columns[6]), delta_color="off")    

    pie_values = [country_df.get(columns[1]).iat[0],country_df.get(columns[2]).iat[0],country_df.get(columns[3]).iat[0],country_df.get(columns[4]).iat[0]]

    pie_labels = [columns[1],columns[2],columns[3],columns[4]]

    fig = px.pie(country_df, values=pie_values, names=pie_labels, hole=0.33)
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    
    st.title("Men - T20i Matches")

    country = "England"

    column1, column2 = st.columns([1,1], gap="small")

    df = pd.read_csv('./pages/dataset/Men T20I Team Batting Stats.csv')

    with column1:
        country = st.selectbox("Country", df['Country'], key="T20i")
        file = './pages/flags/' + country + '.webp'
        st.image(file)
        st.header(country)

    with column2:
        file = './pages/boards/' + country + '.webp'
        image = Image.open(file)
        st.image(image, use_column_width=True)

    country_df = df.loc[df['Country']==country]

    country_df = country_df.drop(['Country'], axis=1)

    columns = country_df.columns

    column1, column2, column3, column4  = st.columns(4, gap='small')

    with column1:
        st.metric(columns[0], country_df.get(columns[0]), delta_color="off")

    with column2:
        st.metric(columns[1], country_df.get(columns[1]), delta_color="off")

    with column3:
        st.metric(columns[2], country_df.get(columns[2]), delta_color="off")    

    with column4:
        st.metric(columns[3], country_df.get(columns[3]), delta_color="off")

    column1, column2, column3, column4  = st.columns(4, gap='small')    

    with column1:
        st.metric(columns[4], country_df.get(columns[4]), delta_color="off")

    with column2:
        st.metric(columns[5], country_df.get(columns[5]), delta_color="off")

    with column3:
        st.metric(columns[9], country_df.get(columns[9]), delta_color="off")    

    with column4:
        st.metric(columns[10], country_df.get(columns[10]), delta_color="off")

    column1, column2, column3  = st.columns([1, 1, 2], gap='small')    

    with column1:
        st.metric(columns[7], country_df.get(columns[7]), delta_color="off")

    with column2:
        st.metric(columns[8], country_df.get(columns[8]), delta_color="off")

    with column3:
        st.metric(columns[6], country_df.get(columns[6]), delta_color="off")    

    pie_values = [country_df.get(columns[1]).iat[0],country_df.get(columns[2]).iat[0],country_df.get(columns[3]).iat[0],country_df.get(columns[4]).iat[0]]

    pie_labels = [columns[1],columns[2],columns[3],columns[4]]

    fig = px.pie(country_df, values=pie_values, names=pie_labels, hole=0.33)
    st.plotly_chart(fig, use_container_width=True)
