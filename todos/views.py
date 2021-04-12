from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView

from todos.forms import CreateTodoForm
from todos.models import Todo


class IndexTemplateView(TemplateView):
    template_name = 'todos/index.html'


class TodoListView(LoginRequiredMixin, ListView):
    context_object_name = 'overdue_tasks'

    def get_queryset(self):
        user = self.request.user
        overdue_tasks = Todo.objects.filter(user=user, due_date__lt=timezone.now()).order_by('due_date')
        return overdue_tasks

    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        overdue_not_done = self.get_queryset().filter(is_done=False).count()
        overdue_done = self.get_queryset().filter(is_done=True).count()
        user = self.request.user
        due_tasks = Todo.objects.filter(user=user, due_date__gte=timezone.now()).order_by('due_date')
        due_not_done = due_tasks.filter(is_done=False).count()
        due_done = due_tasks.filter(is_done=True).count()
        context.update({
            'now': timezone.now(),
            'overdue_not_done': overdue_not_done,
            'overdue_done': overdue_done,
            'due_not_done': due_not_done,
            'due_done': due_done,
            'due_tasks': due_tasks,
        })
        return context


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = CreateTodoForm
    template_name = 'todos/todo_create.html'
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'New task has been created!')
        return super(TodoCreateView, self).form_valid(form)


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todos/todo_delete.html'
    success_url = reverse_lazy('todo_list')



class TodoDoneView(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('todo_list')
    fields = []

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def form_valid(self, form):
        form.instance.is_done = True
        form.save()
        return super(TodoDoneView, self).form_valid(form)

class TodoUndoneView(LoginRequiredMixin, UpdateView):
    success_url = reverse_lazy('todo_list')
    fields = []

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def form_valid(self, form):
        form.instance.is_done = False
        form.save()
        return super(TodoUndoneView, self).form_valid(form)