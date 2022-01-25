import streamlit as st
import pandas as pd

st.set_page_config(page_title="Movie Recommender System")
st.header("Recommendation System")

st.subheader("User Input Features")

@st.cache
def load_data(df1, df2):
    data = pd.read_csv(df1)
    cos_sim = pd.read_csv(df2)
    return data, cos_sim

data, cos_sim = load_data('data.csv', 'cos_sim_data.csv')

st.dataframe(data)