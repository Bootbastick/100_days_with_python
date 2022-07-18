import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "your client id"
CLIENT_SECRET = "your client secret"

date = input("Which year do you want to travel to? Type the date in YYYY-MM-DD format:\n")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

top_100_songs = soup.find_all(name="h3", class_="a-no-trucate")
song_titles_with_nt = [song.getText() for song in top_100_songs]
song_titles = []
for song in song_titles_with_nt:
    song = song.replace("\n", "")
    song = song.replace("\t", "")
    song_titles.append(song)
print(song_titles)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
