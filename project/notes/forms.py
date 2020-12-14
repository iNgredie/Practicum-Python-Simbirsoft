from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from notes.models import Note

User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "name": "email",
                "placeholder": "Email address",
            }
        ),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "password",
                "placeholder": "Password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "password",
                "placeholder": "Confirm password",
            }
        ),
    )
    username = None

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("text",)
        widgets = {"text": forms.Textarea(attrs={"class": "form-control", "rows": 5})}
