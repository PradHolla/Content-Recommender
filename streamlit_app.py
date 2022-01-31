import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide")

background = Image.open("Data/clapper.png")
col1, col2, col3 = st.columns([3, 3, 1])
col2.image(background, width=200)
# st.image("Data/clapper.png", width=200)
st.header("Movie Recommender")
st.write("""
###### This app recommends 5 similar movies to the one you watched. Just enter the movie title and click on the button.
###### This app is based on the IMDb 1000 movies dataset. The dataset is available [here](https://www.kaggle.com/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows).\
 The movie plots are converted into vectors and grouped using the Sentence Transformers Library. Then when the user selects a movie, the app finds 5 nearest vectors\
    using Cosine Similarity and returns the 5 movies.
""")
st.subheader("Enter the movie you watched:")

@st.cache
def load_data(df1, df2):
    data = pd.read_csv(df1)
    cos_sim_data = pd.read_pickle(df2)
    series_title = data['Series_Title'].to_list()
    series_title.insert(0,'')
    return data, cos_sim_data, series_title

def give_recommendations(index,):
    index_recomm = cos_sim_data.loc[index].sort_values(ascending=False).index.tolist()[1:6]
    movies_recomm = data['Series_Title'].loc[index_recomm].values
    released_year = data['Released_Year'].loc[index_recomm].values
    plots = data['Overview'].loc[index_recomm].values
    genres = data['Genre'].loc[index_recomm].values
    rating = data['IMDB_Rating'].loc[index_recomm].values
    return {
        'Movies': movies_recomm,
        'year': released_year,
        'plot': plots,
        'genre': genres,
        'rating': rating,
    }

data, cos_sim_data, series_title = load_data('Data/data.csv', 'Data/cos_sim_data.pkl')

if __name__ == "__main__":
    movie_name = st.selectbox("Start Typing: ", (series_title))
    btn = st.button("Recommendation")
    st.write(movie_name)
    if btn:
        for idx, elm in enumerate(series_title[1:]):
            if elm == movie_name:
                result = (give_recommendations(idx))
        
        for k, movie in enumerate(result['Movies'], start=1):
            st.header(f'The number {k} recommended movie is:')
            st.subheader(f'{movie}({result["year"][k-1]}) - {result["genre"][k-1]}')
            st.write(f'##### {result["plot"][k-1]}')
            st.write(f'##### IMDb Rating: {result["rating"][k-1]}')
            