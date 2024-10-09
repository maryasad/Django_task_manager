# Django_task_manager
## Project Structure
<
task_manager/          # Main project directory
│
├── task_manager/      # Inner directory containing settings and main URLs
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py        # Main URL configuration
│   └── wsgi.py
│
├── tasks/             # Your application directory
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py        # Application-specific URL configuration (create this)
│   ├── views.py       # Define your views here
│   └── templates/     # Folder for HTML templates
│       └── tasks/     # Folder for task-specific templates
│
└── manage.py

>

## Project Setup
*Install Required Software:  
> pip install django djangorestframework django-crispy-forms
* Activat Virtual Environment  
> source venv/bin/activate  
* Create a New Django Project:  
> django-admin startproject task_manager  
> cd task_manager
* Create a New Django App:  
> python manage.py startapp tasks
* Configure Settings:  
  Open task_manager/settings.py and add your new app and required packages to the INSTALLED_APPS list:  
    > 'rest_framework',  # Django REST Framework  
    > 'crispy_forms',    # Crispy Forms  
    > 'tasks',           # Your tasks app  
  > CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Use Bootstrap 4 for crispy forms
## Implementing Features  
1. MTV Architecture:
* Models: Define the Task model in tasks/models.py:
```
from django.db import models
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

```
* Migrate the Database: Run the following commands to create the database tables:
```
python manage.py makemigrations
python manage.py migrate
```
* Views: Create views in tasks/views.py for handling tasks (CRUD operations):
```
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
```

* Templates: Create templates in tasks/templates/tasks/ for listing, creating, updating, and deleting tasks (e.g., task_list.html, task_form.html, task_confirm_delete.html).
* URLs: Define URLs in tasks/urls.py:
* Include the app URLs in task_manager/urls.py:   
2. Django ORM:
  * The Task model already utilizes Django's ORM. You can query the database through the model methods, such as Task.objects.all().
3. Form Handling with Crispy Forms:
* Create a form in tasks/forms.py for handling task creation and updates:
```
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
```




