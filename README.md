# Programming-in-Python-Coursera-
This Python script defines a City class with attributes representing the name, country, elevation, and population of a city. It then creates instances of the City class for three different cities and sets their attributes.

The script also includes a function max_elevation_city that takes a min_population parameter as input. The purpose of this function is to find the city with the highest elevation that meets a certain population threshold. The function evaluates each instance of the City class and returns the name and country of the city that has both an elevation higher than others and a population greater than or equal to min_population.

The function iterates through the instances of the City class (city1, city2, city3) and checks if their population is greater than the given threshold. If so, it compares their elevations to find the city with the highest elevation meeting the population requirement. Finally, it formats and returns the result as a string in the format "City Name, Country".

The provided examples demonstrate the usage of the max_elevation_city function by passing different population thresholds and printing the corresponding results.
