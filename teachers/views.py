from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from webargs.djangoparser import use_args
from webargs import fields
from teachers import forms
from teachers.forms import TeachersCreateForm
from teachers.forms import TeachersFilter
from teachers.models import Teachers


@use_args(
    {
        'first_name': fields.Str(required=False),
        'last_name': fields.Str(required=False),
        'age': fields.Int(required=False),
    },
    location='query'
)
def get_teachers(request, args):
    teachers = Teachers.objects.all()

    for key, value in args.items():
        if value:
            teachers = teachers.filter(**{key: value})

    filter_teachers = TeachersFilter(data=request.GET, queryset=teachers)

    return render(
        request=request,
        template_name='teachers/list.html',
        context={
            'teachers': teachers,
            'filter_teachers': filter_teachers
                 }
    )


def create_teacher(request):
    global form
    if request.method == 'GET':
        form = forms.TeachersCreateForm()
    elif request.method == 'POST':
        form = forms.TeachersCreateForm(data=request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/create.html',
        context={'form': form}
    )


def update_teacher(request, pk):
    teacher = Teachers.objects.get(id=pk)
    if request.method == 'GET':
        form = TeachersCreateForm(instance=teacher)
    elif request.method == 'POST':
        form = TeachersCreateForm(data=request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/update.html',
        context={'form': form}
    )


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teachers, id=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/delete.html', {'teacher': teacher})
