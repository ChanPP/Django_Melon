from django.db import models
from crawler import artist_crawler


class Artist(models.Model):
    BLOOD_TYPE_A = 'a'
    BLOOD_TYPE_B = 'b'
    BLOOD_TYPE_O = 'o'
    BLOOD_TYPE_AB = 'c'
    BLOOD_TYPE_OTHER = 'x'
    CHOICES_BLOOD_TYPE = (
        (BLOOD_TYPE_A, 'A형'),
        (BLOOD_TYPE_B, 'B형'),
        (BLOOD_TYPE_O, 'O형'),
        (BLOOD_TYPE_AB, 'AB형'),
        (BLOOD_TYPE_OTHER, '기타'),
    )

    melon_id = models.CharField("멜론 Artist ID", max_length=20, blank=True, null=True, unique=True)
    img_profile = models.ImageField('프로필 이미지', upload_to='artist', blank=True)
    name = models.CharField('이름', max_length=50)
    real_name = models.CharField('본명', max_length=30, blank=True)
    nationality = models.CharField('국적', max_length=50, blank=True)
    birth_date = models.DateField('생년월일', blank=True, null=True)
    constellation = models.CharField('별자리', max_length=30, blank=True)
    blood_type = models.CharField('혈액형', max_length=1, choices=CHOICES_BLOOD_TYPE, blank=True)
    intro = models.TextField('소개', blank=True)

    def __str__(self):
        return self.name


class Artist_detail:
    def get_artist_detail(self):

        artist_detail = artist_crawler.artist_crawler.melon_artist_crawler(self.name)
        for Artist in artist_detail:
            # if Artist.objects.filter(name=artist_detail['name']).exists():
            #     continue

            Artist.objects.create(
                name=self.name,
                img_profile=Artist['img_profile'],
                real_name=Artist['real_name'],
                nationality=Artist['nationality'],
                birth_date=Artist['birth_date'],
                constellation=Artist['constellation'],
                blood_type=Artist['blood_type'],
                intro=Artist['intro'],
            )
