import requests
from django.core.files import File
from django.shortcuts import redirect
from io import BytesIO
from crawler.album import AlbumData
from ...models import Album