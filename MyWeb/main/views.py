from django.shortcuts import render, redirect, get_object_or_404
from .forms import SearchForm, ContactForm
from .models import Project, AboutMe, ContactMessage
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
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form})
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



def search_view(request):
    form = SearchForm(request.GET)
    results = {
        'projects': [],
        'about_me': [],
    }
    message = None

    if form.is_valid():
        query = form.cleaned_data['query']
        page_mapping = {
            'home': 'home',
            'contact': 'contact',
            'projects': 'projects',
            'about me': 'about_me',
        }

        if query.lower() in page_mapping:
            return redirect(page_mapping[query.lower()])

        results['projects'] = Project.objects.filter(title__icontains=query)
        results['about_me'] = AboutMe.objects.filter(name__icontains=query)

        if not results['projects'] and not results['about_me']:
            message = f'No results found for "{query}".'

    if message:
        return render(request, 'main/home.html', {'form': form, 'message': message, 'results': results})

    return render(request, 'main/home.html', {'form': form, 'results': results})
