from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path

from notes.views import Home, NoteFormView, NoteListView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("create/", login_required(NoteFormView.as_view()), name="create"),
    path("note_list/", login_required(NoteListView.as_view()), name="note_list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
