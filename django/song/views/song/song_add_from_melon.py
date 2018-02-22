from django.shortcuts import render, redirect
from io import BytesIO

from crawler import song_crawler
from ...models import Song

__all__ = (
    'song_add_from_melon',
)


def song_add_from_melon(request):
    if request.method == 'POST':
        song_id = request.POST['song_id']
        song_details = song_crawler.Song_clawler.melon_song_crawler(song_id)

        song_album_img = song_details.get("song_album_img", "")
        song_album = song_details.get("song_album", "")
        song_name = song_details.get("song_name", "")
        song_genre = song_details.get("song_genre", "")
        song_lyrics = song_details.get("song_lyrics", "")
        # response = request.get(song_album_img)
        # binary_data = response.content
        # temp_file = BytesIO()
        # temp_file.seek(0)

        # Song.objects.create({
        #     # Song.album: song_album,
        #     Song.title: song_name,
        #     Song.genre: song_genre,
        #     Song.lyrics: song_lyrics,
        # })

        song = Song(title=song_name, genre=song_genre, lyrics=song_lyrics)
        song.save(force_insert=True)

        return redirect('song:song-list')
