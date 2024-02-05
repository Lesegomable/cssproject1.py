# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:31:36 2024

@author: muamb
"""

import pandas as pd
movie_data = pd.read_csv(r"C:\Users\muamb\.spyder-py3\python\python\.spyproject\movie_dataset.csv")


# Replace columns that has spaces with the ones with underscores
movie_data.columns = movie_data.columns.str.replace(' ', '_')

# Check for any missing values
missing_values = movie_data.isnull().sum()

# Missing values must be filled with mean data values
movie_data['Revenue_(Millions)'].fillna(movie_data['Revenue_(Millions)'].mean(), inplace=True)

# The highest rated movie
highest_rated_movie = movie_data.loc[movie_data['Rating'].idxmax()]

# Extraction the movie title
highest_rated_movie_title = highest_rated_movie['Title']

# The average revenue
average_revenue = movie_data['Revenue_(Millions)'].mean()

# Results
print(f"The average revenue of all movies in the dataset is: {average_revenue:.2f} million dollars.")

# Filter movies from 2015 to 2017
filtered_movies = movie_data[(movie_data['Year'] >= 2015) & (movie_data['Year'] <= 2017)]

# The average revenue for the filtered movies
average_revenue_2015_to_2017 = filtered_movies['Revenue_(Millions)'].mean()

# Results
print(f"The average revenue of movies from 2015 to 2017 is: {average_revenue_2015_to_2017:.2f} million dollars.")

# Number of movies released in the year 2016
movies_2016_count = movie_data[movie_data['Year'] == 2016].shape[0]

# Results
print(f"The number of movies released in the year 2016 is: {movies_2016_count}.")

# Number of movies directed by Christopher Nolan
nolan_movies_count = movie_data[movie_data['Director'] == 'Christopher Nolan'].shape[0]

# Results
print(f"The number of movies directed by Christopher Nolan is: {nolan_movies_count}.")

# Number of movies with a rating of at least 8.0
high_rating_movies_count = movie_data[movie_data['Rating'] >= 8.0].shape[0]

# Results
print(f"The number of movies with a rating of at least 8.0 is: {high_rating_movies_count}.")

# 

# Movies directed by Christopher Nolan
nolan_movies_ratings = movie_data[movie_data['Director'] == 'Christopher Nolan']['Rating']

# Median rating for Christopher Nolan's movies
median_rating_nolan_movies = nolan_movies_ratings.median()

# Results
print(f"The median rating of movies directed by Christopher Nolan is: {median_rating_nolan_movies:.2f}.")




#


# The average rating for each year
average_rating_by_year = movie_data.groupby('Year')['Rating'].mean()

# The year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()

# Get the highest average rating
highest_average_rating = average_rating_by_year.max()

# Results
print(f"The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}.")



#


# Movies from 2006 to 2016
movies_2006_to_2016 = movie_data[(movie_data['Year'] >= 2006) & (movie_data['Year'] <= 2016)]

# Number of movies for each year
movies_count_2006 = movies_2006_to_2016[movies_2006_to_2016['Year'] == 2006].shape[0]
movies_count_2016 = movies_2006_to_2016[movies_2006_to_2016['Year'] == 2016].shape[0]

# The percentage increase
percentage_increase = ((movies_count_2016 - movies_count_2006) / movies_count_2006) * 100

# Print the result
print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%.")



#



from collections import Counter

# Extract and split the actors' names from the "Actors" column
all_actors = movie_data['Actors'].str.split(', ').explode()

# The occurrences of each actor
actor_counts = Counter(all_actors)

# The most common actor
most_common_actor = actor_counts.most_common(1)[0][0]

# Results
print(f"The most common actor in all the movies is: {most_common_actor}.")



#


# Extract and split the genres from the "Genre" column
all_genres = movie_data['Genre'].str.split(', ').explode()

# The number of unique genres
unique_genres_count = all_genres.nunique()

# Results
print(f"The number of unique genres in the dataset is: {unique_genres_count}.")



#


# The correlation matrix for numerical features
correlation_matrix = movie_data.corr()

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Extract insights
insight_1 = "The set of data suggests that the revenue of films is not much influenced by the year of release as this is demonstrated by a sightly weak correlation between Revenue_(Millions) and Year"
insight_2 = "The movies with the higher ratings have higher Metascores, that is there is a positive correlation between Rating and Metascore"
insight_3 = "Movies with higher ratings are more financially successful, this can be seen from the relationship between Rating and Revenue_(Millions)"
insight_4 = "Longer movies do not mean they will have a higher metascore because there is a weak negative correlation between Runtime_(Minutes) and Metascore"
insight_5 = "The level of quality of the movies does not depend on the release year, this is demonstrated by the weak correlation between Rating and Release year"

# Print insights
print("\nInsights:")
print(insight_1)
print(insight_2)
print(insight_3)
print(insight_4)
print(insight_5)
