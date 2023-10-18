import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Team Stats - Bowling")
st.subheader("Developed by Manan Sharma")

tab1, tab2, tab3 = st.tabs(["Tests", "ODIs","T20Is"])

with tab1:   

    st.title("Men - Test Matches")

    country = "England"

    column1, column2 = st.columns([1,1], gap="small")

    df = pd.read_csv('./dataset/Men Test Team Bowling Stats.csv')

    with column1:
        country = st.selectbox("Country", df['Country'], key="Test")
        file = './flags/' + country + '.webp'
        st.image(file)
        st.header(country)

    with column2:
        file = './boards/' + country + '.webp'
        image = Image.open(file)
        st.image(image, use_column_width=True)

    country_df = df.loc[df['Country']==country]

    country_df = country_df.drop(['Country'], axis=1)

    columns = country_df.columns

    column1, column2, column3  = st.columns(3, gap='small')

    with column1:
        st.metric(columns[0], country_df.get(columns[0]), delta_color="off")

    with column2:
        st.metric(columns[1], country_df.get(columns[1]), delta_color="off")

    with column3:
        st.metric(columns[2], country_df.get(columns[2]), delta_color="off")    

    column1, column2 = st.columns([1, 2], gap='small')    

    with column1:
        st.metric(columns[3], country_df.get(columns[3]), delta_color="off")
    
    with column2:
        st.metric(columns[4], country_df.get(columns[4]), delta_color="off")

with tab2:

    st.title("Men - ODI Matches")

    country = "England"

    column1, column2 = st.columns([1,1], gap="small")

    df = pd.read_csv('./dataset/Men ODI Team Bowling Stats.csv')

    with column1:
        country = st.selectbox("Country", df['Country'], key = "ODI")
        file = './flags/' + country + '.webp'
        st.image(file)
        st.header(country)

    with column2:
        file = './boards/' + country + '.webp'
        image = Image.open(file)
        st.image(image, use_column_width=True)

    country_df = df.loc[df['Country']==country]

    country_df = country_df.drop(['Country'], axis=1)
  
    columns = country_df.columns

    column1, column2, column3  = st.columns(3, gap='small')

    with column1:
        st.metric(columns[0], country_df.get(columns[0]), delta_color="off")

    with column2:
        st.metric(columns[1], country_df.get(columns[1]), delta_color="off")

    with column3:
        st.metric(columns[2], country_df.get(columns[2]), delta_color="off")    

    column1, column2 = st.columns([1, 2], gap='small')    

    with column1:
        st.metric(columns[3], country_df.get(columns[3]), delta_color="off")
    
    with column2:
        st.metric(columns[4], country_df.get(columns[4]), delta_color="off")

with tab3:
    
    st.title("Men - T20i Matches")

    country = "England"

    column1, column2 = st.columns([1,1], gap="small")

    df = pd.read_csv('./dataset/Men T20I Team Bowling Stats.csv')

    with column1:
        country = st.selectbox("Country", df['Country'], key="T20i")
        file = './flags/' + country + '.webp'
        st.image(file)
        st.header(country)

    with column2:
        file = './boards/' + country + '.webp'
        image = Image.open(file)
        st.image(image, use_column_width=True)

    country_df = df.loc[df['Country']==country]

    country_df = country_df.drop(['Country'], axis=1)

    columns = country_df.columns

    column1, column2, column3  = st.columns(3, gap='small')

    with column1:
        st.metric(columns[0], country_df.get(columns[0]), delta_color="off")

    with column2:
        st.metric(columns[1], country_df.get(columns[1]), delta_color="off")

    with column3:
        st.metric(columns[2], country_df.get(columns[2]), delta_color="off")    

    column1, column2 = st.columns([1, 2], gap='small')    

    with column1:
        st.metric(columns[3], country_df.get(columns[3]), delta_color="off")
    
    with column2:
        st.metric(columns[4], country_df.get(columns[4]), delta_color="off")
