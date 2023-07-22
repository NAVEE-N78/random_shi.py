import requests#billboardmusikgenerator
from bs4 import BeautifulSoup
date=input("which year you want to travel to YYYY-MM-DD:")
URL =("https://www.billboard.com/charts/hot-100/"+ date)

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')
song_names = soup.select("li ul li h3")
song_name=[song.getText().strip() for song in song_names]
with open("movies.txt", mode="w") as file:
 for song in song_name:
  file.write(f"{song}\n")

