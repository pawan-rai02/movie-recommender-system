# 🎬 Movie Recommender System

A content-based movie recommendation system built with Python and Streamlit that suggests similar movies based on movie metadata.

---

## 📋 Overview

This project analyzes movie data from the TMDB 5000 dataset and recommends movies with similar content. It uses **cosine similarity** on vectorized movie tags (genres, keywords, cast, crew, and overview) to find the most similar movies.

---

## 🚀 Features

- **Content-Based Filtering**: Recommends movies based on content similarity
- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **Top 5 Recommendations**: Displays the 5 most similar movies for any selection
- **Large Dataset**: Trained on 4,800+ movies from TMDB

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas & NumPy | Data manipulation |
| Scikit-learn | Text vectorization & similarity calculation |
| Streamlit | Web application interface |
| Pickle | Model serialization |

---

## 📁 Project Structure

```
movie-recommender-system/
├── code/
│   ├── app.py                      # Streamlit web application
│   ├── movie-recommender-system.ipynb  # Model training notebook
│   ├── movies.pkl                  # Serialized movie data
│   └── similarity.pkl              # Serialized similarity matrix
├── data/
│   ├── tmdb_5000_movies.csv        # Movie metadata
│   └── tmdb_5000_credits.csv       # Cast & crew information
└── README.md
```

---

## 🎯 How It Works

1. **Data Preprocessing**: Movies and credits datasets are merged
2. **Feature Engineering**: Key columns (genres, keywords, cast, crew, overview) are combined into tags
3. **Text Vectorization**: Tags are converted to vectors using CountVectorizer (Bag of Words)
4. **Similarity Calculation**: Cosine similarity matrix is computed between all movies
5. **Recommendation**: For a given movie, find and return the top 5 most similar movies

---

## 🖥️ Streamlit Functions Used

| Function | Purpose |
|----------|---------|
| `st.title()` | Sets the main title of the web app |
| `st.subheader()` | Adds a subtitle/section header |
| `st.selectbox()` | Creates a dropdown menu for movie selection |
| `st.button()` | Creates a clickable button to trigger recommendations |
| `st.write()` | Displays text output (movie titles, messages) |

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd movie-recommender-system
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pandas numpy scikit-learn
   ```

3. **Run the application**
   ```bash
   cd code
   streamlit run app.py
   ```

4. **Open in browser**
   - The app will open automatically at `http://localhost:8501`

---

## 📊 Dataset

The system uses the **TMDB 5000 Movies Dataset** containing:
- Movie metadata (genres, keywords, overview, popularity, etc.)
- Cast and crew information
- Revenue, budget, and ratings

---

## 🎬 Usage

1. Select a movie from the dropdown menu
2. Click the **Recommend** button
3. View the top 5 similar movies based on content similarity

---

## 📝 Notes

- The `movies.pkl` and `similarity.pkl` files are pre-generated from the notebook
- To retrain the model, run all cells in `movie-recommender-system.ipynb`

---

## 👨‍💻 Author
# Pawan Kumar Rai
Built with ❤️ for movie lovers

---
