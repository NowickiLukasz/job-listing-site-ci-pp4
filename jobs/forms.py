from .models import CoverLetter
from django import forms


class CoverLetterForm(forms.ModelForm):
    class Meta:

        model = CoverLetter
        fields = (
            'full_name', 'cover_letter',
        )




