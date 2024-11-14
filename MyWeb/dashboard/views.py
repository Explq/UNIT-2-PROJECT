from django.shortcuts import render
from .models import DashboardItem

def dashboard(request):
    items = DashboardItem.objects.all()
    return render(request, 'dashboard/dashboard.html', {'items': items})
