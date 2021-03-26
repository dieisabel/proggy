__all__ = ['ProfileUpdateForm']


from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Field
from crispy_forms.layout import ButtonHolder
from crispy_forms.layout import Submit

from accounts.models import Profile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image',
            'bio',
            'birthday',
            'twitter_url',
            'custom_url',
            'gender',
        ]
        widgets = {
            'birthday': forms.DateInput(
                format=("%d/%m/%Y"),
                attrs={'placeholder': 'Select a date', 'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('gender', autocomplete='off'),
            Field('bio', autocomplete='off'),
            Field('birthday', autocomplete='off'),
            Field('twitter_url', autocomplete='off'),
            Field('custom_url', autocomplete='off'),
            Field('image', autocomplete='off'),
            ButtonHolder(
                Submit('submit', 'Update')
            )
        )
