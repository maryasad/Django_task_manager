**Task Manager Application**

This application allows users to create, update, delete, and view tasks. Each task can have a title, description, and a status.

### Project Setup

1. **Install Required Software**:
   Make sure you have Python and Django installed. You also need to install the Django REST Framework and Django Crispy Forms.

   ```bash
   pip install django djangorestframework django-crispy-forms
   ```

2. **Create a New Django Project**:
   
   ```bash
   django-admin startproject task_manager
   cd task_manager
   ```

3. **Create a New Django App**:
   Create a new app within your project to handle tasks:

   ```bash
   python manage.py startapp tasks
   ```

4. **Configure Settings**:
   Open `task_manager/settings.py` and add your new app and required packages to the `INSTALLED_APPS` list:

   ```python
   INSTALLED_APPS = [
       ...,
       'rest_framework',  # Django REST Framework
       'crispy_forms',    # Crispy Forms
       'tasks',           # Your tasks app
   ]

   CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Use Bootstrap 4 for crispy forms
   ```

### Implementing Features

#### 1. **MTV Architecture**:

- **Models**:
  Define the `Task` model in `tasks/models.py`:

  ```python
  from django.db import models

  class Task(models.Model):
      title = models.CharField(max_length=100)
      description = models.TextField(blank=True)
      completed = models.BooleanField(default=False)

      def __str__(self):
          return self.title
  ```

- **Migrate the Database**:
  Run the following commands to create the database tables:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Views**:
  Create views in `tasks/views.py` for handling tasks (CRUD operations):

  ```python
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

- **Templates**:
  Create templates in `tasks/templates/tasks/` for listing, creating, updating, and deleting tasks (e.g., `task_list.html`, `task_form.html`, `task_confirm_delete.html`).

  Example for `task_list.html`:

  ```html
  {% load crispy_forms_tags %}
  <!DOCTYPE html>
  <html>
  <head>
      <title>Task Manager</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  </head>
  <body>
      <div class="container">
          <h1>Task List</h1>
          <a href="{% url 'task_create' %}" class="btn btn-primary">Add Task</a>
          <ul class="list-group mt-3">
              {% for task in tasks %}
              <li class="list-group-item d-flex justify-content-between align-items-center">
                  {{ task.title }}
                  <div>
                      <a href="{% url 'task_update' task.pk %}" class="btn btn-warning btn-sm">Edit</a>
                      <a href="{% url 'task_delete' task.pk %}" class="btn btn-danger btn-sm">Delete</a>
                  </div>
              </li>
              {% endfor %}
          </ul>
      </div>
  </body>
  </html>
  ```

- **URLs**:
  Define URLs in `tasks/urls.py`:

  ```python
  from django.urls import path
  from .views import task_list, task_create, task_update, task_delete

  urlpatterns = [
      path('', task_list, name='task_list'),
      path('task/create/', task_create, name='task_create'),
      path('task/update/<int:pk>/', task_update, name='task_update'),
      path('task/delete/<int:pk>/', task_delete, name='task_delete'),
  ]
  ```

  Include the app URLs in `task_manager/urls.py`:

  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('tasks.urls')),
  ]
  ```

#### 2. **Django ORM**:
- The `Task` model already utilizes Django's ORM. You can query the database through the model methods, such as `Task.objects.all()`.

#### 3. **Form Handling with Crispy Forms**:
- Create a form in `tasks/forms.py` for handling task creation and updates:

  ```python
  from django import forms
  from .models import Task

  class TaskForm(forms.ModelForm):
      class Meta:
          model = Task
          fields = ['title', 'description', 'completed']
  ```

  Use `crispy_forms` in your templates to render the form:

  ```html
  <form method="POST">
      {% csrf_token %}
      {{ form|crispy }}
      <button type="submit" class="btn btn-primary">Save</button>
  </form>
  ```

#### 4. **Django REST Framework**:
- Create a serializer in `tasks/serializers.py`:

  ```python
  from rest_framework import serializers
  from .models import Task

  class TaskSerializer(serializers.ModelSerializer):
      class Meta:
          model = Task
          fields = '__all__'
  ```

- Create API views in `tasks/views.py`:

  ```python
  from rest_framework import viewsets
  from .models import Task
  from .serializers import TaskSerializer

  class TaskViewSet(viewsets.ModelViewSet):
      queryset = Task.objects.all()
      serializer_class = TaskSerializer
  ```

- Add URLs for the API in `tasks/urls.py`:

  ```python
  from rest_framework.routers import DefaultRouter
  from .views import TaskViewSet

  router = DefaultRouter()
  router.register(r'api/tasks', TaskViewSet)

  urlpatterns += router.urls
  ```

#### 5. **Security Features**:
- **CSRF Protection**: Django has built-in CSRF protection enabled by default for forms using `{% csrf_token %}` in templates.
- **XSS Protection**: Use Django’s template system, which auto-escapes variables to prevent XSS.
- **Authentication**: You can use Django’s built-in authentication system or create custom authentication views for securing your API.

### Final Steps

1. **Run the Server**:
   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

2. **Access Your Application**:
   - Open your browser and navigate to `http://127.0.0.1:8000/` to see the Task Manager.
   - Access the API at `http://127.0.0.1:8000/api/tasks/`.

### Conclusion

This project covers the core concepts of Django, including the MTV architecture, ORM, form handling, Django REST Framework, and essential security features. As you progress, consider enhancing your application with user authentication, task due dates, or task categories.

Feel free to ask if you need more details on any of these steps or if you'd like to explore additional features!
