from django.contrib import admin

from todos.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['task', 'user', 'due_date']
    search_fields = ['task']
    list_filter = ['due_date']


admin.site.register(Todo, TodoAdmin)
