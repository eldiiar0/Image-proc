from django import forms
from .models import UploadedImage

class UploadImageForm(forms.ModelForm):

    class Meta:
        model = UploadedImage
        fields = ('image',)

        widgets = {
            "image": forms.FileInput(attrs={"rows": "", "class": "form-control m-3 custom-file-label"}),
        }