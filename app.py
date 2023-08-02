import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movies_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&append_to_response=images'.format(movies_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']


def recomend(movie):
    movies_index=movies[movies['title']==movie].index[0]
    distances=similarity[movies_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movies_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster
        recommended_movies_poster.append(fetch_poster(movies_id))
    return recommended_movies,recommended_movies_poster

movies_dic=pickle.load(open('movies_dic.pkl','rb'))
movies=pd.DataFrame(movies_dic)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recomended System')


selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)

if st.button('Recommend'):
    names,posters=recomend(selected_movie_name)

    col1, col2, col3,col4,col5 = st.columns(5)

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




