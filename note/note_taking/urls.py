from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # Note Path
    path('note-list/', views.note_list, name='note-list'),
    path('create-note/', views.create_note, name='create-note'),
    path('note-detail/<str:pk>', views.note_detail, name='note-detail'),
    path('edit-note/<str:pk>', views.update_note, name='edit-note'),
    path('delete-note/<str:pk>', views.delete_note, name='delete-note'),
    path('generate-pdf/<str:pk>', views.generate_pdf, name='generate-pdf'),
    # Note Type path
    path('note-type-list/', views.note_type_list, name='note-type-list'),
    path('note-type-detail/<str:pk>', views.note_type_detail, name='note-type-detail'),
    path('create-note-type/', views.create_note_type, name='create-note-type'),
    path('edit-note-type/<str:pk>', views.update_note_type, name='edit-note-type'),
    path('delete-note-type/<str:pk>', views.delete_note_type, name='delete-note-type'),
    
    
]
