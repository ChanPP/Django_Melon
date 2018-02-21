from django.shortcuts import render
from crawler import song_crawler
__all__ =(
    'song_add_from_melon',
)


def song_add_from_melon(request):
    if request.method == 'POST':
        song_id = request.POST['song_id']
        song_details = song_crawler.Song_clawler.melon_song_crawler(song_id)
        
        return render(request)