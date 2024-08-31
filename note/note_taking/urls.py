from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('note-list/', views.note_list, name='note-list'),
    path('create-note/', views.create_note, name='create-note'),
    path('note-detail/<str:pk>', views.note_list, name='note-detail'),
]
