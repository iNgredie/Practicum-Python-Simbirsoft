from django import forms
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.forms import UserCreationForm

from notes.models import Note

User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password")
    password2 = forms.CharField(label="Confirm password")
    username = None

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            auth_user = authenticate(
                email=self.cleaned_data["email"],
                password=self.cleaned_data["password1"],
            )
            login(self.request, auth_user)

        return user


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ("text",)
        widgets = {"text": forms.Textarea(attrs={"class": "form-control", "rows": 5})}
