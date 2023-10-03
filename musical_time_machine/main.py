import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from os import environ

load_dotenv()
# Input: Prompt user to go back to which date in the past (Format: YYYY-MM-DD)
## Condition for valid date_interest.
## 1. Must follow the format
## 2. Must be in the past
date_interest = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Scrape the Billboard chart 100 of the given day
URL = f"https://www.billboard.com/charts/hot-100/{date_interest}/"


response = requests.get(url=URL)

soup_scrape = BeautifulSoup(response.text, "html.parser")

soup_scrape = soup_scrape.select("li h3[id='title-of-a-story']")

hit_songs = [song.getText().strip() for song in soup_scrape]

# Connect to Spotify without user authentication
scope = "playlist-modify-private"

APP_CLIENT_ID=environ["APP_CLIENT_ID"]
CLIENT_SECRET=environ["CLIENT_SECRET"]
REDIRECT_URI="http://example.com"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=APP_CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope))

# Create a playlist
playlist_id = sp.user_playlist_create(user=environ["user"], name=f"Hot 100 in the Past on {date_interest}", public=False)["id"]

uri_list = []
for song in hit_songs:
    try:
        result = sp.search(q=song, type="track", limit=1)
    except:
        pass
    else:
        for idx, track in enumerate(result["tracks"]["items"]):
            uri_list.append(track["uri"])

# Add tracks to a playlist
sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)
