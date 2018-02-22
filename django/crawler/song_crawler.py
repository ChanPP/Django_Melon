import os
import requests
from bs4 import BeautifulSoup, NavigableString

'''
class MelonCrawler:
    def search_song(self, q):
        url = 'https://www.melon.com/search/song/index.htm'
        params = {
            'q': q,
            'section': 'song',
        }
        response = requests.get(url, params)
        soup = BeautifulSoup(response.text, 'lxml')
        tr_list = soup.select('form#frm_defaultList table > tbody > tr')
        # tr_list = soup.find('form', id='frm_defaultList').find('table').find('tbody').find_all('tr')

        result = []
        for tr in tr_list:
            # <a href="javascript:searchLog('web_song','SONG','SO','빨간맛','30512671');melon.play.playSong('26020103',30512671);" class="fc_gray" title="빨간 맛 (Red Flavor)">빨간 맛 (Red Flavor)</a>
            # song_id = re.search(r"searchLog\(.*'(\d+)'\)", tr.select_one('td:nth-of-type(3) a.fc_gray').get('href')).group(1)
            song_id = tr.select_one('td:nth-of-type(1) input[type=checkbox]').get('value')
            title = tr.select_one('td:nth-of-type(3) a.fc_gray').get_text(strip=True)
            artist = tr.select_one('td:nth-of-type(4) span.checkEllipsisSongdefaultList').get_text(
                strip=True)
            album = tr.select_one('td:nth-of-type(5) a').get_text(strip=True)

            song = Song(song_id=song_id, title=title, artist=artist, album=album)
            result.append(song)

        return result


class Song:
    def __init__(self, song_id, title, artist, album):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.album = album

        self._release_date = None
        self._lyrics = None
        self._genre = None
        self._producers = None

    def __str__(self):
        return f'{self.title} (아티스트: {self.artist}, 앨범: {self.album})'

    def get_detail(self):
        url = 'https://www.melon.com/search/song/index.htm'
        params = {
            'q': q,
            'section': 'song',
        }
        response = requests.get(url, params)
        soup = BeautifulSoup(response.text, 'lxml')
        div_entry = soup.find('div', class_='entry')
        title = div_entry.find('div', class_='song_name').strong.next_sibling.strip()
        artist = div_entry.find('div', class_='artist').get_text(strip=True)
        # 앨범, 발매일, 장르...에 대한 Description list
        dl = div_entry.find('div', class_='meta').find('dl')
        # isinstance(인스턴스, 클래스(타입))
        # items = ['앨범', '앨범명', '발매일', '발매일값', '장르', '장르값']
        items = [item.get_text(strip=True) for item in dl.contents if not isinstance(item, str)]
        it = iter(items)
        description_dict = dict(zip(it, it))

        album = description_dict.get('앨범')
        release_date = description_dict.get('발매일')
        genre = description_dict.get('장르')

        div_lyrics = soup.find('div', id='d_video_summary')

        lyrics_list = []
        for item in div_lyrics:
            if item.name == 'br':
                lyrics_list.append('\n')
            elif type(item) is NavigableString:
                lyrics_list.append(item.strip())
        lyrics = ''.join(lyrics_list)

        # 리턴하지말고 데이터들을 자신의 속성으로 할당
        self.title = title
        self.artist = artist
        self.album = album
        self._release_date = release_date
        self._genre = genre
        self._lyrics = lyrics
        self._producers = {}


if __name__ == '__main__':
    crawler = MelonCrawler()
    q = input('검색할 곡 명을 입력해주세요: ')
    search_song_list = crawler.search_song(q)
    for i in search_song_list:
        print(i)
'''


class Song_clawler:

    def __init__(self, song_album_img, song_album, song_name,
                 song_genre, song_lyrics, song_id):
        self.song_album_img = song_album_img
        self.song_album = song_album
        self.song_name = song_name
        self.song_genre = song_genre
        self.song_lyrics = song_lyrics
        self.song_id = song_id

    def melon_song_crawler(song_id):
        URL = f'https://www.melon.com/song/detail.htm?songId={song_id}'

        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "lxml")

        song_album_img = soup.find("div", {"class": "thumb"}).a.img["src"].strip()[:-59]
        song_album = soup.find("div", {"class": "meta"}).dl.dd.a.text
        song_name = soup.find("meta", {"property": "og:title"})["content"]
        song_genre = soup.find("div", {"class": "meta"}).findAll("dd")[2].text
        song_lyrics = soup.find("div", {"id": "d_video_summary"}).text
        # song_lyrics = song_lyrics.lstrip()
        # song_lyrics = song_lyrics.rstrip()

        song_search_list = ({
            "song_album_img": song_album_img,
            "song_album": song_album,
            "song_name": song_name,
            "song_genre": song_genre,
            "song_lyrics": song_lyrics
        })
        return song_search_list


if __name__ == "__main__":
    song_id = input("song_id를 입력하세요")
    song_crawler = Song_clawler.melon_song_crawler(song_id)
    print(song_crawler)