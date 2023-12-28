import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv('tmdb_movies.csv')
df_genres = pd.read_csv('tmdb_genres.csv')
top_rated_movies = df_movies[df_movies['vote_count'] > df_movies['vote_count'].quantile(0.75)]
top_10 = top_rated_movies.sort_values(by='vote_average', ascending=False).head(10)
print(top_10[['title', 'vote_average']])
