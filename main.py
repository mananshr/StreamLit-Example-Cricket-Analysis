import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('./dataset/Men Test Team Batting Stats.csv')

st.title("Team Batting Stats - Men")
st.subheader("Developed by Manan Sharma")
st.divider()

country = "England"

column1, column2 = st.columns([1,1], gap="small")

with column1:
    country = st.selectbox("Country", df['Country'])
    file = './flags/' + country + '.webp'
    st.image(file)
    st.header(country)

with column2:
    file = './boards/' + country + '.webp'
    image = Image.open(file)
    # image = image.resize((300, 300))
    # image_width, image_height = image.size
    # image_dim = image_width if image_height<image_width else image_height
    # st.image(image, width=image_dim, use_column_width=True)
    st.image(image, use_column_width=True)

# values = np.array()

country_df = df.loc[df['Country']==country]

# st.write(country_df.get('Team Matches Played'))

country_df = country_df.drop(['Country'], axis=1)

columns = country_df.columns

column1, column2, column3, column4  = st.columns(4, gap='small')

# print(columns)

# for column in columns:
#     st.metric(column, country_df.get(column), delta_color="off")

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

# values = np.array([country_df.get(columns[1]),country_df.get(columns[2]),country_df.get(columns[3]),country_df.get(columns[4])])

pie_values = [country_df.get(columns[1]).iat[0],country_df.get(columns[2]).iat[0],country_df.get(columns[3]).iat[0],country_df.get(columns[4]).iat[0]]

# print(country_df.get(columns[1]).iat[0])
# print(country_df.get(columns[1]).at[0,0])

pie_labels = [columns[1],columns[2],columns[3],columns[4]]

# pie_colors = ["#00A659", "#F21A29", "#0060A9", "#FFDA3D"]

# plt.pie(pie_values, labels=pie_labels)
# plt.legend()

# st.pyplot(plt, use_container_width=True)

fig = px.pie(country_df, values=pie_values, names=pie_labels, hole=0.33)
st.plotly_chart(fig, use_container_width=True)

# i = 0
# for cols in columns:
#     print(i)
#     print(cols)
#     i += 1