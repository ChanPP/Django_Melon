from django.shortcuts import render
from django.shortcuts import redirect
from crawler import song_crawler
from ...models import Song

__all__ = (
    'song_add_from_melon',
)


def song_add_from_melon(request):
    # 패키지 분할 (artist랑 똑같은 형태로)
    # artist_add_from_melon과 같은 기능을 함
    #   song_search_from_melon도 구현
    #       -> 이 안에 'DB에 추가'하는 Form구현
    if request.method == "POST":
        song_id = request.POST['song_id']
        return render(request)
