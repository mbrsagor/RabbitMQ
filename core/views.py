from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


class GenerateRandomUserView(FormView):
    template_name = 'core/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('/')


class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'user_list.html'
