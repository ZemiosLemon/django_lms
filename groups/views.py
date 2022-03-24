from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse

from groups import forms
from groups.forms import GroupCreateForm
from groups.forms import GroupsFilter
from webargs.djangoparser import use_args
from webargs import fields
from groups.models import Group


@use_args(
    {
        'name_group': fields.Str(required=False),
        'size_group': fields.Int(required=False),
    },
    location='query'
)
def get_group(request, args):
    groups = Group.objects.all()

    for key, value in args.items():
        if value:
            groups = groups.filter(**{key: value})

    filter_groups = GroupsFilter(data=request.GET, queryset=groups)

    return render(
            request=request,
            template_name='groups/list.html',
            context={
                'groups': groups,
                'filter_groups': filter_groups
            }
        )


def create_groups(request):
    global form
    if request.method == 'GET':
        form = forms.GroupCreateForm()
    elif request.method == 'POST':
        form = forms.GroupCreateForm(data=request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


def update_groups(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST, instance=group)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/update.html',
        context={'form': form,
                 'group': group}
    )


def delete_groups(request, pk):
    group = get_object_or_404(Group, id=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
