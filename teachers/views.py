from django.http import HttpResponseRedirect
from django.shortcuts import render
from webargs.djangoparser import use_args
from webargs import fields
from teachers import forms
from teachers.forms import TeachersCreateForm
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

    return render(
        request=request,
        template_name='teachers/list.html',
        context={'teachers': teachers}
    )


# @csrf_exempt
def create_teacher(request):
    global form
    if request.method == 'GET':
        form = forms.TeachersCreateForm()
    elif request.method == 'POST':
        form = forms.TeachersCreateForm(data=request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/teachers/')

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
            return HttpResponseRedirect('/teachers/')

    return render(
        request=request,
        template_name='teachers/update.html',
        context={'form': form}
    )
