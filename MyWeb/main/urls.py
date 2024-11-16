from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about_me, name='about_me'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:pk>/update/', views.update_project, name='update_project'),
    path('projects/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('search/', views.search_view, name='search_view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
