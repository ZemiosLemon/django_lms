from django import forms
from django_filters import FilterSet

from .models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name_group',
            'size_group',

        ]


class GroupsFilter(FilterSet):
    class Meta:
        model = Group
        fields = {
            'size_group': ['exact'],
            'name_group': ['exact', 'startswith']
        }
