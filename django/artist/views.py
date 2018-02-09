from django.shortcuts import render

from .models import Artist


def artist_list(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists,
    }
    return render(
        request,
        'artist/artist_list.html',
        context,
    )


def artist_add(request):
    # names = Artist.objects.filter(name=name),
    # real_name = Artist.objects.filter(real_name=real_name),
    # birth_date = Artist.objects.filter(birth_date=birth_date)
    # nationality = Artist.objects.filter(nationality=nationality),
    # constrllation = Artist.objects.filter(constrllation=constrllation),
    # blood_type = Artist.objects.filter(blood_type=blood_type),
    # intro = Artist.objects.filter(intro=intro)
    # contexts = Artist.objects.all()
    # contexts = {
    #     'names': names,
    #     'real_name': real_name,
    #     'nationality': nationality,
    #     'birth_date': birth_date,
    #     'constellation': constrllation,
    #     'blood_type': blood_type,
    #     'intro': intro,
    # }
    # artist_adds = Artist.objects.all()
    # contexts = {
    #     'name': artist_adds.name,
    #     'real_name': artist_adds.real_name,
    #     'nationality': artist_adds.nationality,
    #     'birth_date': artist_adds.birth_date,
    #     'constellation': artist_adds.constellation,
    #     'blood_type': artist_adds.blood_type,
    #     'intro': artist_adds.intro,
    # }
    if request.method == 'GET':
        pass
    else:
        return render(request, 'artist/artist_add')
