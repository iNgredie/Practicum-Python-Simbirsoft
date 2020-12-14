from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, FormView, ListView

from notes.forms import NoteForm, RegistrationForm
from notes.models import Note


class Home(ListView):
    model = Note
    template_name = "index.html"
    context_object_name = "note_list"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.model.objects.filter(owner=self.request.user)


class RegisterFormView(FormView):
    form_class = RegistrationForm
    success_url = "/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        email = self.request.POST["email"]
        password = self.request.POST["password1"]
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse("home"))

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class NoteFormView(CreateView):
    form_class = NoteForm
    success_url = "/note_list/"
    template_name = "note_edit.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        self.object = form.save()
        return super(NoteFormView, self).form_valid(form)


class NoteListView(ListView):
    model = Note
    template_name = "note_list.html"
    context_object_name = "note_list"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.model.objects.filter(owner=self.request.user)
