from django.db import models

__all__ = (
    'ArtistUouTube',
)


class ArtistUouTube(models.Model):
    youtube_id = models.CharField('YouTube ID', primary_key=True, max_length=20)
    title = models.CharField('제목', max_length=200)
