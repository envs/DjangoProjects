import numpy as np
import pandas as pd

# data = pd.read_csv('/Users/dinance/Downloads/EE/OpenVINO/ml-25m/ratings.csv')
data = pd.read_csv('/Users/dinance/Desktop/Bots/PyMicroservice/DjangoProjects/workshoppers/recommender/ml-latest-small/ratings.csv')

movie_titles_genre = pd.read_csv("/Users/dinance/Desktop/Bots/PyMicroservice/DjangoProjects/workshoppers/recommender/ml-latest-small/movies.csv")

data = data.merge(movie_titles_genre, on='movieId', how='left')

# Average rating for each & every movie
Average_ratings = pd.DataFrame(data.groupby('title')['rating'].mean())

# Total ratings for a movie
Average_ratings['Total Ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())
#print(Average_ratings.head(10))

# Calculating the Correlation
movie_user = data.pivot_table(index='userId', columns='title', values='rating')

# Let's choose a movie and see its correlation value (pairwise correlation) with other movies
correlations = movie_user.corrwith(movie_user['Toy Story (1995)'])

# Now, let's remove all the empty values and merge the total ratings to the correlation table
recommendation = pd.DataFrame(correlations, columns=['Correlation'])
recommendation.dropna(inplace=True)
recommendation = recommendation.join(Average_ratings['Total Ratings'])

# Let's test the recommendation system. Let's filter all movies with correlation value to 
# Toy Story (1995), and with at least 100 ratings
recc = recommendation[recommendation['Total Ratings']>100].sort_values('Correlation', ascending=False).reset_index()

# Let's also merge the movies dataset for verifying the recommendations
recc = recc.merge(movie_titles_genre, on='title', how='left')
print(recc.head(10))