import requests
from bs4 import BeautifulSoup
keyword = "likey"
URL = f'https://www.melon.com/search/song/index.htm?q={keyword}&section=&searchGnbYn=Y&kkoSpl=Y&kkoDpType=&ipath=srch_form'

response = requests.get(URL)
soup = BeautifulSoup(response.text, "lxml")
# form_list = soup.find("form", {"id":"frm_searchSong"}).find("tbody").findAll("tr")
form_lists = soup.find("div", {"class": "tb_list"}).tbody.findAll("tr")
# songs = form_lists[0].find("div", {"class": "ellipsis"}).findAll("a")[1]["title"]
# artists = form_lists[0].find("div", {"id": "artistName"}).span.text
# albums = form_lists[0].find("div", {"class": "ellipsis"}).a.b.text
# album = form_lists[0].findAll("td")[4].a.text

song_search_list = []
for form_list in form_lists:
    print(form_list)
    song = form_list.find("div", {"class": "ellipsis"}).findAll("a")[1]["title"]
    print(song)
    artist = form_list.find("div", {"id": "artistName"}).span.text
    artist_album = form_list.findAll("td")[4].a.text
    song_id = form_list.find("div").input["value"]
    song_search_list.append({
        "song": song,
        "artist": artist,
        "artist_album": artist_album,
        "song_id": song_id,
    })

print(song_search_list)