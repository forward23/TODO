from django import forms
from todos.models import Todo


class DateInput(forms.DateTimeInput):
    input_type = 'date'



class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'due_date']
        widgets = {'due_date': DateInput()}


