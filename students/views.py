from django.http import HttpResponse, HttpResponseRedirect
from lms.utils import format_records
from students.models import Students
from webargs.djangoparser import use_args
from webargs import fields
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentsCreateForm

def index(request):
    return HttpResponse('<h1>Hello!</h1>')


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

    html_form = """
        <form method="get">
            <label for="first_name">First name:</label>
            <input type="text" id="first_name" name="first_name"></br></br>

            <label for="last_name">Last name:</label>
            <input type="text" id="last_name" name="last_name"></br></br>

            <label for="age">Age:</label>
            <input type="number" id="age" name="age"></br></br>

            <input type="submit" value="Submit">
        </form>
    """

    records = format_records(students)

    response = html_form + records

    return HttpResponse(response)



@csrf_exempt
def create_student(request):
    global form
    if request.method == 'GET':
        form = StudentsCreateForm()
    elif request.method == 'POST':
        form = StudentsCreateForm(data=request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/students/')

    html_form = f"""
                <form method="post">
                    {form.as_p()}
                    <input type="submit" value="Submit">
                </form>
                """
    return HttpResponse(html_form)