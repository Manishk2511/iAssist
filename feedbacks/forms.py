from django import forms
from .models import Feedback_list, problem


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback_list
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['problem'].empty_label = "Select"
        self.fields['location'].required = False
