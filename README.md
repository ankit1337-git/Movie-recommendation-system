# 🎬 Movie Recommendation System

This project is a content-based movie recommendation system built using Python and Streamlit. It recommends movies that are similar to the one selected by the user by comparing movie metadata such as genres, cast, crew, keywords, and overview.

To make the recommendations more engaging, the application also fetches movie posters in real time using the TMDB API.

---

## 🚀 Demo

*(Add your Streamlit app link here after deployment.)*

---

## ✨ Features

- Recommend 5 similar movies instantly
- Fetch movie posters using the TMDB API
- Simple and responsive Streamlit interface
- Content-based recommendation using cosine similarity
- Handles missing posters gracefully

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Requests
- Pickle

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── app.py
├── movies.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

> **Note:** `similarity.pkl` is not included in this repository because it exceeds GitHub's file size limit.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ankit1337-git/TV-show-recommendation-system.git
```

Move into the project folder:

```bash
cd TV-show-recommendation-system
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movies Dataset** for building the recommendation engine.

---

## 🧠 How it Works

1. Movie features are combined into a single text representation.
2. Text is converted into vectors.
3. Cosine similarity is calculated between movies.
4. The five most similar movies are recommended.
5. Posters are fetched dynamically using the TMDB API.

---

## 📌 Future Improvements

- Deploy the application online
- Add movie search functionality
- Improve recommendation quality using hybrid filtering
- Add filters based on genre, language, and release year

---

## 👨‍💻 Author

**Ankit**

If you have any suggestions or feedback, feel free to connect with me on LinkedIn

## 📸 Screenshots

### Home Page
![Home](images/home.png)

### Search
![Search](images/search.png)

### Recommendations
![Recommendations](images/recommendations.png)

## 🚀 Live Demo

https://movie-recommendation-system-i5z4ravbwnwhsbvpmldqwu.streamlit.app/
