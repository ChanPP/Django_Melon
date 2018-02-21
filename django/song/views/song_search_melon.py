from django.shortcuts import render

__all__ = (
    'artist_search_from_melon',
)


def artist_search_from_melon(request):
    keyword = request.GET.get("keyword")
    context = {}
    if keyword:
        import requests
        from bs4 import BeautifulSoup
        URL = f'https://www.melon.com/search/song/index.htm?q={keyword}&section=&searchGnbYn=Y&kkoSpl=Y&kkoDpType=&ipath=srch_form'

        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "lxml")
        # form_list = soup.find("form", {"id":"frm_searchSong"}).find("tbody").findAll("tr")
        form_lists = soup.find("div", {"class": "tb_list"}).tbody.findAll("tr")
        # songs = form_lists[0].find("div", {"class": "ellipsis"}).findAll("a")[1]["title"]
        # artists = form_lists[0].find("div", {"id": "artistName"}).span.text
        # albums = form_lists[0].find("div", {"class": "ellipsis"}).a.b.text
        album = form_lists[0].findAll("td")[4].a.text
        print(album)

        song_search_list = []
        for form_list in form_lists:
            song = form_list.find("div", {"class": "ellipsis"}).findAll("a")[1]["title"]
            artist = form_list.find("div", {"id": "artistName"}).span.text
            artist_album = form_list.findAll("td")[4].a.text
            song_search_list.append({
                "song": song,
                "artist": artist,
                "artist_album": artist_album,
            })
        context['song_search_list'] = song_search_list
    return render(request, 'song/song_search_form_melon.html')
