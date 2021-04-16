from django import forms
from complaints.models import problem, complaint
from .models import status_list, user_status_list


class user_status_form(forms.ModelForm):
    class Meta:
        model = user_status_list
        fields = ('status', 'complaint_id')

    def __init__(self, *args, **kwargs):
        super(user_status_form, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Select"


class status_form(forms.ModelForm):
    class Meta:
        model = status_list
        fields = ('status', 'complaint_id')

    def __init__(self, *args, **kwargs):
        super(status_form, self).__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Select"
