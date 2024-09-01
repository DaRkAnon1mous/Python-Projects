# Geo Plotter Project - Visualizing USA Cities 🌎

Welcome to the Geo Plotter Project! This project leverages the power of NumPy, Pandas, Matplotlib, and Folium to create interactive maps that visualize various cities across the USA. 📍

## Project Overview

In this project, I used a CSV file containing data of various cities in the USA, including their locations (latitude and longitude) and population. 

The goal was to create a visual representation of this data on a map, with markers indicating the cities' locations, and marker colors reflecting the population size.

## Features
- Interactive Map: The map allows users to zoom in/out and explore different regions of the USA.
- Color-Coded Markers: Cities are marked with different colors based on their population:
   - Red 🔴: Population greater than 35,000
   - Blue 🔵: Population between 10,000 and 35,000
   - Green 🟢: Population less than 10,000
- Pop-ups: Clicking on a marker reveals a pop-up with the city’s name and population.

## How It Works
- Data Processing: The CSV file is processed using Pandas to extract relevant information such as city names, latitudes, longitudes, and populations.

- Marker Color Function: A custom function determines the color of the marker based on the population size:

- Red 🔴 for cities with a population greater than 35,000

- Blue 🔵 for cities with a population between 10,000 and 35,000

- Green 🟢 for cities with a population less than 10,000

- Map Creation: The map is created using Folium, where markers are added for each city based on their geographical coordinates.

## Results
The result is an interactive map of the USA with cities marked in various colors, providing an intuitive visual representation of population distribution across the country.

![image](https://github.com/user-attachments/assets/1b4361ac-13f0-4af0-a16f-63846289fcbe)

![image](https://github.com/user-attachments/assets/5882ffca-91ab-41c7-97f3-59ff3e707a7b)

![image](https://github.com/user-attachments/assets/c281c62d-9b54-4fe3-84f2-e0d3a81df349)

![image](https://github.com/user-attachments/assets/ada2f11e-bf3a-41db-a52c-3decccea5b6e)

![image](https://github.com/user-attachments/assets/2a3d8e69-824a-4c9e-b07e-cdc1bf58ceff)

## Conclusion

This project demonstrates the capabilities of Python’s data manipulation and visualization libraries to create meaningful geographical representations of data. Explore the map, and gain insights into the population distribution of cities across the USA! 🌍

Thank you for exploring the Geo Plotter Project! Feel free to reach out with any questions or feedback. 😊

### 🔗 Resources

NumPy Documentation

Pandas Documentation

Matplotlib Documentation

Folium Documentation

Happy Mapping! 📊🗺️
