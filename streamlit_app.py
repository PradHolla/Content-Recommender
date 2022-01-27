import streamlit as st
import pandas as pd

st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide")
st.header("Recommendation System")

st.subheader("User Input Features")

@st.cache
def load_data(df1, df2):
    data = pd.read_csv(df1)
    cos_sim_data = pd.read_pickle(df2)
    series_title = data['Series_Title'].to_list()
    series_title.insert(0,'')
    return data, cos_sim_data, series_title

def give_recommendations(index,print_recommendation=False,print_recommendation_plots=False,print_genres=False):
    index_recomm = cos_sim_data.loc[index].sort_values(ascending=False).index.tolist()[1:6]
    movies_recomm = data['Series_Title'].loc[index_recomm].values
    result = {'Movies':movies_recomm,'Index':index_recomm}
    if print_recommendation==True:
        st.write('The watched movie is this one: %s \n'%(data['Series_Title'].loc[index]))
        for k, movie in enumerate(movies_recomm, start=1):
            st.header('The number %i recommended movie is this one: %s \n'%(k,movie))
            # for k, q in enumerate(range(len(movies_recomm)), start=1):
            #     plot_q = data['Overview'].loc[index_recomm[q]]
            #     genre = data['Genre'].loc[index_recomm[q]]   
            #     st.subheader('Plot:  \n %s \n'%(plot_q))
            #     st.subheader('Genre:  \n %s \n'%(genre))
            #     q
    if print_recommendation_plots==True:
        # st.write('The plot of the watched movie is this one:  \n %s \n'%(data['Overview'].loc[index]))
        for k, q in enumerate(range(len(movies_recomm)), start=1):
            plot_q = data['Overview'].loc[index_recomm[q]]
            st.write('The plot of the number %i recommended movie is this one:  \n %s \n'%(k,plot_q))
    if print_genres==True:
        # st.write('The genres of the watched movie is this one:\n %s \n'%(data['Genre'].loc[index]))
        for k, q in enumerate(range(len(movies_recomm)), start=1):
            plot_q = data['Genre'].loc[index_recomm[q]]
            st.write('The plot of the number %i recommended movie is this one:  \n %s \n'%(k,plot_q))
    return result

data, cos_sim_data, series_title = load_data('data.csv', 'cos_sim_data.pkl')

movie_name = st.selectbox("Enter a movie name: ", (series_title))
btn = st.button("Recommendation")
st.write(movie_name)
if btn:
    for idx, elm in enumerate(series_title[1:]):
        if elm == movie_name:
            st.write(idx)
            ret = (give_recommendations(idx,True,True,True))
            
