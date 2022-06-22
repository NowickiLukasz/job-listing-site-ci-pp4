from .models import CoverLetter, JobListing
from django import forms
from django_summernote.widgets import SummernoteWidget


class CoverLetterForm(forms.ModelForm):
    class Meta:

        model = CoverLetter
        fields = (
            'jobs', 'cover_letter',
        )

        widgets = {
            'cover_letter': SummernoteWidget(attrs={'class': 'form-control'}),
        }


class AddJobListingForm(forms.ModelForm):
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
            # 'employer': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'postition_type': forms.Select(attrs={'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'class': 'form-control'}),
            
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
            'postition_type': forms.Select(attrs={'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'class': 'form-control'}),
            
        }


