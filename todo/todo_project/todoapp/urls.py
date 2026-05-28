
from todoapp import views
from django.urls import path
urlpatterns = [
    
path('', views.home, name='home'),
path('add-task', views.add_task, name='add-task'),
path('mark-as-done/<int:id>/', views.mark_as_done, name='mark_as_done'),
path('delete/<int:id>/', views.delete_task, name='delete'),
]
