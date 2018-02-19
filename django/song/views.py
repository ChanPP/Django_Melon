from django.http import HttpResponse
from django.shortcuts import render

from .models import Song


def song_list(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    return render(
        request,
        'song/song_list.html',
        context,
    )


def song_search(request):
    if request.method == "POST":
        keyword = request.POST['keyword']
        return HttpResponse(keyword)

    elif request.method == "GET":
        return render(request, 'song/song_search.html')

    '''
    사용 할 URL:song/search/
    사용할 Template: templates/song/song_search.html
        form안에
            input한개, button한개 배치
    1. song/urls.py에 URL작성
    2. templates/song/song_search.html작성
        {% extends %} 사용할것
    3. 이 함수에서 return render(...)
    :param request:
    :param title:
    :return:
    '''
