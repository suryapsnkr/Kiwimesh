from django.urls import path
from mesh.views import Notes, GetNote, Query

urlpatterns = [
    path('notes/', Notes.as_view(), name='addNote'),
    path('notes/<int:pk>', GetNote.as_view(), name='getNote'),
    path('notes/<str:title>', Query.as_view(), name='query'),
]