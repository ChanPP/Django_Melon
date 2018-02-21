import requests
from bs4 import BeautifulSoup
# keyword = 30636089
# URL = f'https://www.melon.com/song/detail.htm?songId={keyword}'
#
# response = requests.get(URL)
# soup = BeautifulSoup(response.text, "lxml")
#
# song_album_img = soup.find("div", {"class": "thumb"}).a.img["src"].strip()[:-59]
# song_album = soup.find("div", {"class": "meta"}).dl.dd.a.text
# song_name = soup.find("meta", {"property": "og:title"})["content"]
# song_genre = soup.find("div", {"class": "meta"}).findAll("dd")[2].text
# song_lyrics = soup.find("div", {"id": "d_video_summary"}).text
#
# song_search_list = ({
#     "song_album_img": song_album_img,
#     "song_album": song_album,
#     "song_name": song_name,
#     "song_genre": song_genre,
#     "song_lyrics": song_lyrics
# })
#
# print(song_search_list)


import requests
from bs4 import BeautifulSoup
keyword = "가을아침"
URL = f'https://www.melon.com/search/song/index.htm?q={keyword}&section=&searchGnbYn=Y&kkoSpl=Y&kkoDpType=&ipath=srch_form'

response = requests.get(URL)
soup = BeautifulSoup(response.text, "lxml")
# form_list = soup.find("form", {"id":"frm_searchSong"}).find("tbody").findAll("tr")
form_lists = soup.find("div", {"class": "tb_list"}).tbody.findAll("tr")
# songs = form_lists[0].find("div", {"class": "ellipsis"}).findAll("a")[1]["title"]
# artists = form_lists[0].find("div", {"id": "artistName"}).span.text
# albums = form_lists[0].find("div", {"class": "ellipsis"}).a.b.text
album = form_lists[0].findAll("td")[4].a.text

song_search_list = []
for form_list in form_lists:
    song = form_list.find("div", {"class": "ellipsis"}).findAll("a")[1]["title"]
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