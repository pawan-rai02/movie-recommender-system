import streamlit as st
import pickle
import os

st.title('Movie Recommender System')
st.subheader('Content Based Recommender System')

movies_path = os.path.join(os.path.dirname(__file__), 'movies.pkl')
similarity_path = os.path.join(os.path.dirname(__file__), 'similarity.pkl')

movies_df = pickle.load(open(movies_path, 'rb'))
similarity = pickle.load(open(similarity_path, 'rb'))

movie_list = movies_df['title'].values

# function to recommend movies
def recommend(movie):
    movie_idx = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_idx]
    
    recommended_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    for i in recommended_movies:
        st.write(movies_df.iloc[i[0]].title)


option = st.selectbox('Select a movie from the dropdown', movie_list)

if st.button('Recommend'):
    st.subheader('Top 5 similar movies to ' + option + ' are:')
    recommend(option)

