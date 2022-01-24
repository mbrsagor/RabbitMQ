import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery import shared_task

from .models import Todo


@shared_task
def create_random_users(total):
    for user in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@dev.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return f'Random users created with success! {total}'


@shared_task
def create_todo(title=None, details=None):
    task = Todo.objects.create(title=title, details=details)
    task.save()
