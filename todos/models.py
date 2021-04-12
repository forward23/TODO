from django.conf import settings
from django.db import models
from django.urls import reverse


class Todo(models.Model):
    task = models.CharField(max_length=250)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} {self.task}'

    # def get_success_url(self):
    #     return reverse('todo_list')


