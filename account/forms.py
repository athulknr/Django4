from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import User,JobPosting,Job,Application
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = ('username','email','password1','password2','is_admin','is_employee','is_employer')
class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['description', 'experience', 'email', 'gender']

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','short_description','long_description']   

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content','experience']            