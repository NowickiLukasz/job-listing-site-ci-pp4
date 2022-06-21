from .models import CoverLetter, JobListing
from django import forms


class CoverLetterForm(forms.ModelForm):
    class Meta:

        model = CoverLetter
        fields = (
            'full_name', 'cover_letter',
        )


class AddJobListingForm(forms.ModelForm):
    """
        Styling for the add job function
    """
    class Meta:

        model = JobListing
        fields = (
            'title', 'employer', 'location', 'salary', 'postition_type',
            'description',
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'employer': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'postition_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            
        }


class EditJobListingForm(forms.ModelForm):
    """
        Styling for the add job function
    """
    class Meta:

        model = JobListing
        fields = (
            'title', 'location', 'salary', 'postition_type',
            'description',
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'employer': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'postition_type': forms.Textarea(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            
        }


