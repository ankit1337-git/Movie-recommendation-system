import streamlit as st
import pickle
import requests
import time
import os
import gdown

FILE_ID = "1KoIICFUHh2GcWIAa9hZ856qk7TSUzPrw"

if not os.path.exists("similarity.pkl"):
    gdown.download(
        f"https://drive.google.com/uc?id={FILE_ID}",
        "similarity.pkl",
        quiet=False
    )

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>

/* Hide Streamlit menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

.stButton>button{
    width:100%;
    border-radius:10px;
    height:48px;
    font-size:16px;
    font-weight:600;
}

header {visibility:hidden;}

/* Main background */
.stApp{
    background-color:#0E1117;
}

/* Title */
.main-title{
    font-size:55px;
    color:white;
    text-align:center;
    font-weight:bold;
}

.subtitle{
    color:#BBBBBB;
    text-align:center;
    font-size:20px;
    margin-bottom:30px;
}

/* Button */
.stButton>button{
    width:100%;
    background:#E50914;
    color:white;
    border:none;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#B20710;
}

/* Images */
img{
    border-radius:15px;
}
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#111827);
    color:white;
}
[data-testid="stVerticalBlock"]{
background:rgba(255,255,255,.08);
border-radius:20px;
padding:20px;
backdrop-filter:blur(12px);
}


</style>
""", unsafe_allow_html=True)
API_KEY = st.secrets["TMDB_API_KEY"]
def poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    for _ in range(3):
        try:
            response = requests.get(
                url,
                timeout=10,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            response.raise_for_status()

            data = response.json()

            poster_path = data.get("poster_path")

            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"

            return None

        except requests.exceptions.RequestException:
            time.sleep(1)

    return None

def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies =[]
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]]["id"]
        recommended_movies.append(movies.iloc[i[0]].original_title)
        recommended_movies_poster.append(poster(movie_id))
    return recommended_movies, recommended_movies_poster


with open("movies.pkl", "rb") as f:
    movies = pickle.load(f)

movie_list = movies["original_title"].tolist()

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

st.title("🎬 Movie Recommendation System")
st.caption("Discover movies similar to your favorites.")

option = st.selectbox(
    "Select your movie",
     movie_list,
     index=None,
     placeholder="movie...",
)
if st.button("Get Recommendations"):
    if option is None:
        st.warning("Please select a movie first.")
    else:
        with st.spinner("Finding recommendations..."):
            names, posters = recommend(option)

        cols = st.columns(5)

        for col, name, poster_url in zip(cols, names, posters):
            with col:
                if poster_url:
                    st.image(poster_url, use_container_width=True)
                else:
                    st.info("No poster")

                st.caption(name)
        st.divider()

        st.caption("Built using Python, Streamlit and Scikit-Learn")