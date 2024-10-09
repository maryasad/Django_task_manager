from django.urls import path
from .views import task_list, task_create, task_update, task_delete
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

urlpatterns = [
    path('', task_list, name='task_list'),
    path('task/create/', task_create, name='task_create'),
    path('task/update/<int:pk>/', task_update, name='task_update'),
    path('task/delete/<int:pk>/', task_delete, name='task_delete'),
]
router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet)

urlpatterns += router.urls
