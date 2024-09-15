import pandas as pd
import streamlit as st
import requests
st.set_page_config(layout="wide")

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=0852db99d5e85a682a4a798f341d8ece&language=en-US".format(movie_id));
    data = response.json();
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


st.title("Movue Recommender system")



import pickle
movie_list = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movie_list)

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    (movies['title'].values))

st.write("You selected:", selected_movie_name)

similarity = pickle.load(open('similarity.pkl','rb'));


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_list_sorted = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:11]

    movie_names_recommended = [];
    recommended_movies_poster = [];
    for i in movie_list_sorted:
        #fetch poster from API
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id));
        movie_names_recommended.append(movies.iloc[i[0]].title)

    return movie_names_recommended,recommended_movies_poster

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[5])
        st.image(posters[5])
    with col2:
        st.text(names[6])
        st.image(posters[6])
    with col3:
        st.text(names[7])
        st.image(posters[7])
    with col4:
        st.text(names[8])
        st.image(posters[8])
    with col5:
        st.text(names[9])
        st.image(posters[9])
