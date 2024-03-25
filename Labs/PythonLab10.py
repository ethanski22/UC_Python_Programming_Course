import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series

# Read the data
sh_raw = pd.read_csv('movies.csv', 
	 header=None, 
	 names=['Year','Title','Comic','IMDB','RT','','OpeningWeekendBoxOffice','AvgTicketPriceThatYear','EstdOpeningAttendance','USPopThatYear'])

# Clean the data
sh = sh_raw[np.isfinite(sh_raw.OpeningWeekendBoxOffice)]

# Print the first 5 rows
print(sh.head(5))

# Normalize and scatterplot the scores
imdb_normalized = sh.IMDB / 10         
sh.insert(10,'IMDBNormalized',imdb_normalized)
rt_normalized = sh.RT/100        
sh.insert(11, 'RTNormalized', rt_normalized)
sh.plot.scatter(x ='RTNormalized', y ='IMDBNormalized')
plt.show(block=False)

# Print the correlation and summary statistics
print(sh[['RTNormalized','IMDBNormalized']].corr())
print(sh[['RTNormalized','IMDBNormalized']].describe())
print()

# Answer to the questions

# 1. Print the Series rows for the 'DC' comic movies
dc_movies = sh[sh['Comic'] == 'DC']
print(dc_movies)
print()

# 2. Print the Year and Title columns of only 'DC' comic movies
print(dc_movies[['Year', 'Title']])
print()

# 3. Print the Year and Title columns of only 'Marvel' movies
marvel_movies = sh[sh['Comic'] == 'Marvel']
print(marvel_movies[['Year', 'Title']])
print()

# 4. Plot a scatterplot for AvgTicketPriceThatYear vs. Year
sh.plot.scatter(x='Year', y='AvgTicketPriceThatYear')
plt.show(block=False)

# 5. Print the correlation for the Year versus the AvgTicketPriceThatYear
correlation = sh[['Year', 'AvgTicketPriceThatYear']].corr()
print(correlation)
print()

# 6. Print the summary statistics for OpeningWeekendBoxOffice
print(sh['OpeningWeekendBoxOffice'].describe())
