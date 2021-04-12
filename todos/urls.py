from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('todos/', views.TodoListView.as_view(), name='todo_list'),
    path('todos/create', views.TodoCreateView.as_view(), name='todo_create'),
    path('todos/<int:pk>/delete', views.TodoDeleteView.as_view(), name='todo_delete'),
    path('todos/<int:pk>/done', views.TodoDoneView.as_view(), name='todo_done'),
    path('todos/<int:pk>/undone', views.TodoUndoneView.as_view(), name='todo_undone'),

]