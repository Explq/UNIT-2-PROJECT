from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about_me, name='about_me'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:pk>/update/', views.update_project, name='update_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),


]
