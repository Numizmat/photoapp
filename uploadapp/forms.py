from django import forms
from .models import Image, Save, SaveImg


class SaveForm(forms.ModelForm):
    class Meta:
        model = Save
        fields = ['text']


class SaveImgForm(forms.ModelForm):
    image_field = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = SaveImg
        fields = ['image']


class ImageForm(forms.ModelForm):
    photo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Image
        fields = ('title', 'photo', 'annotation')
