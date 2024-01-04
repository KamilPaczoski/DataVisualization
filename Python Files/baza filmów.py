import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv('tmdb_movies.csv')
df_genres = pd.read_csv('tmdb_genres.csv')
top_rated_movies = df_movies[df_movies['vote_count'] > df_movies['vote_count'].quantile(0.75)]
top_10 = top_rated_movies.sort_values(by='vote_average', ascending=False).head(10)
print(top_10[['title', 'vote_average']])

df_movies['release_year'] = pd.to_datetime(df_movies['release_date']).dt.year
filtered_movies = df_movies[(df_movies['release_year'] >= 2010) & (df_movies['release_year'] <= 2016)]

data = filtered_movies.groupby('release_year').agg({'revenue': 'mean', 'budget': 'mean'})


def milion(x, pos):
    return '{:2.1f}M'.format(x * 1e-6)


fig = plt.figure(figsize=(10, 5))
ax = fig.add_axes([0.1, 0.1, 0.7, 0.8])
ax.bar(data.index, data['revenue'], color='blue', label='Mean Revenue')
ax.plot(data['budget'], color='red', marker='o', label='Mean Budget')
ax.yaxis.set_major_formatter(plt.FuncFormatter(milion))
ax.set_title('Średni budżet i przychód filmów w latach 2010-2016')
ax.legend(loc=(1.05, 0.90))

plt.show()

df_movies_genres = pd.merge(df_movies, df_genres, left_on='genre_id', right_index=True, how="inner",
                            validate="many_to_many")

most_of_genre = df_movies_genres['genres'].value_counts().idxmax()
amout = {most_of_genre: df_movies_genres['genres'].value_counts().max()}
print(f'{most_of_genre}:{amout}')

avarage_runtime = df_movies_genres.groupby('genres')['runtime'].mean()
longest_runtime = {avarage_runtime.idxmax(): avarage_runtime.max()}
print(longest_runtime)

longest_genre = df_movies_genres[
    df_movies_genres['genres'] == next(iter(longest_runtime))]  # tak mogłem w słowniki się nei bawić :P
plt.figure(figsize=(10, 5))
plt.hist(longest_genre['runtime'], color='orchid', bins=40)
plt.show()
