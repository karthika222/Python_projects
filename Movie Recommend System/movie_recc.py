import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
m=pd.read_csv("tmdb_5000_movies.csv")
m=m[['title','genres','keywords','overview']]
m.fillna('',inplace=True)
m['tags']=m['genres']+' '+m['keywords']+' '+m['overview']
cv=CountVectorizer(max_features=5000,stop_words='english')
vectors=cv.fit_transform(m['tags'].values).toarray()
similarity=cosine_similarity(vectors)
def recommend(movie):
    movie_index=m[m['title']==movie].index[0]
    dist=similarity[movie_index]
    m_list=sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]
    for i in m_list:
        print(m.iloc[i[0]].title)
mn=input("Enter movie name: ")
recommend(mn)











