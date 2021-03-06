from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse

from students.models import Students
from webargs.djangoparser import use_args
from webargs import fields

from .forms import StudentsCreateForm
from .forms import StudentsFilter


@use_args(
    {
        'first_name': fields.Str(required=False),
        'last_name': fields.Str(required=False),
        'age': fields.Int(required=False),
    },
    location='query'
)
def get_students(request, args):
    students = Students.objects.all()

    for key, value in args.items():
        if value:
            students = students.filter(**{key: value})

    filter_students = StudentsFilter(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={
            'students': students,
            'filter_students': filter_students,
        }
    )


def create_student(request):
    global form
    if request.method == 'GET':
        form = StudentsCreateForm()
    elif request.method == 'POST':
        form = StudentsCreateForm(data=request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/create.html', {'form': form})


def update_student(request, pk):
    student = Students.objects.get(id=pk)
    if request.method == 'GET':
        form = StudentsCreateForm(instance=student)
    elif request.method == 'POST':
        form = StudentsCreateForm(data=request.POST, instance=student)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/update.html',
        context={'form': form}
    )


def delete_students(request, pk):
    student = get_object_or_404(Students, id=pk)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': student})
