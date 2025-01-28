from django import forms
from django.contrib.auth.models import User
from .models import Task

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")
        return cleaned_data


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date'
    }))

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'due_date',
            'priority',
            'status',
            'project'
        ]
