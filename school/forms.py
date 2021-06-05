from django import forms
from django.contrib.auth.models import User
from . import models


# for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


# for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = models.StudentExtra
        fields = ['university', 'education', 'mobile','image',
                  'college', 'college_aggregate', 'college_year_of_passing',
                  'school', 'school_aggregate', 'school_year_of_passing',
                  'hsc', 'hsc_aggregate', 'hsc_year_of_passing',
                  ]


# for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class RecruterExtraForm(forms.ModelForm):
    class Meta:
        model = models.RecruterExtra
        fields = ['mobile', 'status']


# for notice related form


# for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
