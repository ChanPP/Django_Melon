from django.forms import ModelForm, forms
from requests import request

from artist.models import Artist

__all__ = (
    'ArtistForm',
)


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['melon_id', 'name', 'real_name', 'img_profile',
                  'nationality', 'birth_date', 'constellation',
                  'blood_type', 'intro']

        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #         }
        #     )
        # }
