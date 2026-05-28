
from todoapp import views
from django.urls import path
urlpatterns = [
    
path('', views.home, name='home'),
path('add-task', views.add_task, name='add-task'),
path('mark-as-done/<int:id>/', views.mark_as_done, name='mark_as_done'),
path('mark-as-undone/<int:id>/', views.mark_as_undone, name='mark_as_undone'),
path('delete/<int:id>/', views.delete_task, name='delete'),
path('delete_completed_task/<int:id>/', views.delete_completed_task, name='delete_completed_task'),
path('edit_task/<int:id>/', views.edit_task, name='edit_task'),


]
