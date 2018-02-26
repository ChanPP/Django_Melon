from django import forms

from artist.models import Artist

__all__ = (
    'ArtistForm',
)


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['melon_id', 'name', 'real_name', 'img_profile',
                  'nationality', 'birth_date', 'constellation',
                  'blood_type', 'intro']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }
