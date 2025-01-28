from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                 # Landing page
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('task-list/', views.task_list, name='task_list'),
    path('task-create/', views.task_create, name='task_create'),
    path('task-edit/<int:task_id>/', views.task_edit, name='task_edit'),
    path('task-delete/<int:task_id>/', views.task_delete, name='task_delete'),
]
