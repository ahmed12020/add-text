from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Student
from ckeditor.widgets import CKEditorWidget

class UserUpdateForm(UserChangeForm):
    password = None
    # email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}


class StudentForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Student
        fields = ['name','title','body']

