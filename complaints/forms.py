from django import forms
from .models import problem, Complaints, image_upload


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = ('problem', 'desciption', 'area', 'pincode', 'image')
        labels = {
            'area': 'Location',
        }

    def __init__(self, *args, **kwargs):
        super(ComplaintForm, self).__init__(*args, **kwargs)
        self.fields['problem'].empty_label = "Select"
        self.fields['area'].required = False


class ImageForm(forms.ModelForm):
    class Meta:
        model = image_upload
        fields = ('image',)
