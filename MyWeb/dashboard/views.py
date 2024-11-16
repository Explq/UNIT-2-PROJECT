from django.shortcuts import render
from .models import DashboardItem
from main.models import Project, AboutMe, ContactMessage
def dashboard(request):
    items = DashboardItem.objects.all()
    projects = Project.objects.all()
    about_me = AboutMe.objects.first()
    contact_messages = ContactMessage.objects.all()
    context = {
        'items': items,
        'projects': projects,
        'about_me': about_me,
        'contact_messages': contact_messages,
    }

    return render(request, 'dashboard/dashboard.html', context)
