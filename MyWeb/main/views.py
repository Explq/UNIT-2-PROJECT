from django.shortcuts import render, redirect, get_object_or_404
from .forms import SearchForm
from .models import Project, AboutMe
from django.contrib import messages
from .forms import ProjectForm


def home(request):
    form = SearchForm(request.GET)
    results = None
    if 'query' in request.GET and request.GET['query']:
        query = request.GET['query']
        results = {
            'projects': Project.objects.filter(title__icontains=query),
            'about_me': AboutMe.objects.filter(name__icontains=query),
        }

    return render(request, 'main/home.html', {'form': form, 'results': results})

def about_me(request):
    about = AboutMe.objects.first()
    return render(request, 'main/about_me.html', {'about': about})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main/projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        messages.success(request, 'Your message has been sent successfully!')

        return render(request, 'main/contact.html')
    return render(request, 'main/contact.html')

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project added successfully!')
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'main/add_project.html', {'form': form})


def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully!')
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'main/update_project.html', {'form': form, 'project': project})

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully!')
        return redirect('projects')
    return render(request, 'main/delete_project.html', {'project': project})