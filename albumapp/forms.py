from django import forms
from uploadapp.models import Image




class AlbumForm(forms.ModelForm):
    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Image
        fields = ('title', 'photo', 'annotation')