from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, UpdateView

from .forms import CustomUserChangeForm

CustomUser = get_user_model()

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    # form_class = CustomUserChangeForm
    fields = ['username', 'first_name', 'last_name', 'email', 'age', 'city', 'avatar']
    template_name = 'account/profile.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.kwargs['pk']})







class PasswordUpdateView(UpdateView):
    pass
