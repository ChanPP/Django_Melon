from django.shortcuts import redirect, render

from ...models import Album

__all__ = (
    'album_add'
)


def album_add(request):
    if request.method == "POST":
        title = request.POST["title"]
        Album.objects.create(
            title=title,
        )
        return redirect('album:album-list.html')
    else:
        return render(request, "album/album_add.html")
