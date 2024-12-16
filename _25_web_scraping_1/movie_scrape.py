from bs4 import BeautifulSoup
import  requests
import lxml

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2")
empire_movies = response.text
# print(empire_movies)
soup = BeautifulSoup(empire_movies, "lxml")
movie_names = soup.select("span h2 strong")
movies = [movie.getText() for movie in movie_names]
movies_title = movies[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies_title:
        file.write(f"{movie}\n")