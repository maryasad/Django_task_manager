# Django_task_manager
*Install Required Software:  
-pip install django djangorestframework django-crispy-forms
* Activat Virtual Environment  
-source venv/bin/activate  
* Create a New Django Project:  
.django-admin startproject task_manager  
.cd task_manager
* Create a New Django App:  
-python manage.py startapp tasks
* Configure Settings:  
  Open task_manager/settings.py and add your new app and required packages to the INSTALLED_APPS list:
    'rest_framework',  # Django REST Framework
    'crispy_forms',    # Crispy Forms
    'tasks',           # Your tasks app
  CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Use Bootstrap 4 for crispy forms


INSTALLED_APPS = [
    ...,
    'rest_framework',  # Django REST Framework
    'crispy_forms',    # Crispy Forms
    'tasks',           # Your tasks app
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Use Bootstrap 4 for crispy forms



