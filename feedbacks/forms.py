from django import forms
from .models import Feedback, problem


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['problem'].empty_label = "Select"
        self.fields['location'].required = False
