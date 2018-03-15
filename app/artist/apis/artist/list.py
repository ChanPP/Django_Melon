import json

from django.http import JsonResponse, HttpResponse

from artist.models import Artist

__all__ = (
    'artist_list',
)


def artist_list(request):
    """
    data: {
        'artist': [
            {
                'melon_id':.. ,
                'name': ..
            },
            {
                'melon_id':.. ,
                'name': ..
            }
            ...
        ]
    }
    :param request:
    :return:
    """
    artists = Artist.objects.all()
    data = {'artist': [{'melon_id': artist.melon_id, 'name': artist.name} for artist in artists]}

    # for artist in artists:
    #     data.append({'melon_id': artist.melon_id,
    #                  'name': artist.name})

    # return HttpResponse(json.dumps(data), content_type='application/json')
    return JsonResponse(data)

# /artist/       -> artist.urls.views
# /api/artist/   -> artist.urls.apis

# /album/        -> album.urls.views
# /api/album/    -> album.urls.apis
