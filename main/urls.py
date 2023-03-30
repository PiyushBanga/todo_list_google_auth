from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo_list/', views.todo_list, name='todo_list'),
    path('todo_item/<int:id>/', views.todo_item, name='todo_item'),
    path('add_todo_item/', views.add_todo_item, name='add_todo_item'),
    path('edit_todo_item/<int:id>/', views.edit_todo_item, name='edit_todo_item'),
    path('delete_todo_item/<int:id>/', views.delete_todo_item, name='delete_todo_item'),
]