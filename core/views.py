from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm, TodoForm
from .tasks import create_random_users, create_todo


class GenerateRandomUserView(FormView):
    template_name = 'core/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_users.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('/users/')


class UserListView(ListView):
    model = User
    ordering = '-id'
    context_object_name = 'users'
    template_name = 'user_list.html'


class TaskCreateView(FormView):
    template_name = 'core/create_todo.html'
    form_class = TodoForm

    def form_valid(self, form):
        pass
