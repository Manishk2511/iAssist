from django import forms
from .models import problem, complaint


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = complaint
        fields = ('problem', 'desciption', 'area', 'pincode')
        labels = {
            'area': 'Location',
        }

    def __init__(self, *args, **kwargs):
        super(ComplaintForm, self).__init__(*args, **kwargs)
        self.fields['problem'].empty_label = "Select"
        self.fields['area'].required = False
