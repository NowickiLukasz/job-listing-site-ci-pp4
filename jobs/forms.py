from allauth.account.forms import SignupForm
from .models import CoverLetter, JobListing, UserProfile
from django import forms
from django_summernote.widgets import SummernoteWidget


class CoverLetterForm(forms.ModelForm):
    class Meta:

        model = CoverLetter
        fields = (
            'cover_letter',
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
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'postition_type': forms.Select(attrs={'class': 'form-control'}),
            'description': SummernoteWidget(attrs={'class': 'form-control'}),
            
        }


class EditUserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = (
            'title', 'date_of_birth', 'country', 'gender', 'bio'
        )

        widgets = {

                'title': forms.Select(attrs={'class': 'form-control'}),
                'location': forms.TextInput(attrs={'class': 'form-control'}),
                'country': forms.Select(attrs={'class': 'form-control'}),
                'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
                'gender': forms.Select(attrs={'class': 'form-control'}),
                'bio': SummernoteWidget(attrs={'class': 'form-control'}),
                
            }

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30, label='First Name', 
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(
        max_length=30, label='Last Name', 
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

   
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user