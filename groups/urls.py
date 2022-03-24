
from django.urls import path

from .views import create_groups
from .views import delete_groups
from .views import get_group
from .views import update_groups

app_name = 'groups'

urlpatterns = [
    path('', get_group, name='list'),
    path('create/', create_groups, name='create'),
    path('update/<int:pk>/', update_groups, name='update'),
    path('delete/<int:pk>/', delete_groups, name='delete'),
]