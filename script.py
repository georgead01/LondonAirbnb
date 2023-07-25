import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy.stats import gamma, kstest, normaltest

data = pd.read_csv("/Users/georgead/Documents/Projects/LondonAirbnb/London_Airbnb_Listings_March_2023.csv")
data['price'] = data['price'].apply(lambda x: float(x[1:].replace(',','')))

print(data)

plt.title('Airbnb Rentals in London')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.scatter(data['longitude'], data['latitude'], s = 0.1)
plt.scatter(-0.090985, 51.512344, c = 'r')
plt.show()

filtered_data = data.loc[(data['room_type'] == 'Private room') | (data['room_type'] == 'Entire home/apt')]
category_colors = (filtered_data['room_type'] == 'Private room').apply(lambda x: 'C0' if x else 'C1')

plt.title('Airbnb Rentals in London by Type of Room')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.scatter(filtered_data['longitude'], filtered_data['latitude'], s = 0.1, c = category_colors)
plt.show()

room_data = data[data['room_type'] == 'Private room']
apt_data = data[data['room_type'] == 'Entire home/apt']

plt.title('Room Prices Distribution Histogram')
plt.xlabel('Price ($)')
plt.hist(room_data['price'], range=(0,999), bins = 100)
plt.show()

plt.title('Entire Unit Prices Distribution Histogram')
plt.xlabel('Price ($)')
plt.hist(apt_data['price'], range=(0,999), bins = 100)
plt.show()