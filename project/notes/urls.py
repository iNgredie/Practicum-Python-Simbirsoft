from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from notes.views import Home, NoteFormView, NoteListView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("create/", NoteFormView.as_view(), name="create"),
    path("note_list/", NoteListView.as_view(), name="note_list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
