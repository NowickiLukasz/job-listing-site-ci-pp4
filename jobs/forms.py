from .models import CoverLetter
from django import forms



class CoverLetterForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = (
            'cover_letter',
        )
