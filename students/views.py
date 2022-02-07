from django.http import HttpResponse
from faker import Faker
from lms.utils import format_records
from students.models import Students
from webargs.djangoparser import use_kwargs
from webargs import fields


def index(request):
    return HttpResponse('<h1>Hello!</h1>')


@use_kwargs(
    {
        'count': fields.Integer(required=False, missing=10)
    },
    location='query'
)
def generate_students(request, count):
    fake = Faker()
    for _ in range(count):
        stud = Students(first_name=fake.first_name(),
                        last_name=fake.last_name(), age=fake.pyint(15, 75))
        stud.save()
    students = Students.objects.all()
    result = format_records(students)
    return HttpResponse(result)
