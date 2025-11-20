from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# -------- Original Code ---------
m = pd.read_csv("tmdb_5000_movies.csv")
m = m[['title', 'genres', 'keywords', 'overview']]
m.fillna('', inplace=True)
m['tags'] = m['genres'] + ' ' + m['keywords'] + ' ' + m['overview']

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(m['tags'].values).toarray()
similarity = cosine_similarity(vectors)
# --------------------------------


def recommend(movie):
    movie_index = m[m['title'].str.lower() == movie.lower()].index[0]
    dist = similarity[movie_index]
    m_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = [m.iloc[i[0]].title for i in m_list]
    return recommended


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend_movie():
    movie_name = request.form['movie']
    try:
        recommendations = recommend(movie_name)
        return render_template('result.html', movie=movie_name, recommendations=recommendations)
    except IndexError:
        return render_template('result.html', movie=movie_name, recommendations=[], error="Movie not found!")


if __name__ == '__main__':
    app.run(debug=True)
