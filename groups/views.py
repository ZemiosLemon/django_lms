from django.http import HttpResponseRedirect
from django.shortcuts import render
from groups import forms
from groups.forms import GroupCreateForm
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
    return render(
            request=request,
            template_name='groups/list.html',
            context={'groups': groups}
        )


# @csrf_exempt
def create_groups(request):
    global form
    if request.method == 'GET':
        form = forms.GroupCreateForm()
    elif request.method == 'POST':
        form = forms.GroupCreateForm(data=request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/groups/')

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
            return HttpResponseRedirect('/groups')

    return render(
        request=request,
        template_name='groups/update.html',
        context={'form': form}
    )
