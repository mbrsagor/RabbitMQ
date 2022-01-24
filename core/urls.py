from django.urls import path
from .views import GenerateRandomUserView, UserListView

urlpatterns = [
    path('', GenerateRandomUserView.as_view(), name='random_user_generate'),
    path('users/', UserListView.as_view(), name='use_list'),
]
