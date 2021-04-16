from django import forms
from government.models import area_problem_selection, area_available, problem_available


class area_problem_form(forms.ModelForm):
    class Meta:
        model = area_problem_selection
        fields = ('area_selection', 'problem_selection')

    def __init__(self, *args, **kwargs):
        super(area_problem_form, self).__init__(*args, **kwargs)
        self.fields['area_selection'].empty_label = "Select"
        self.fields['problem_selection'].empty_label = "Select"
