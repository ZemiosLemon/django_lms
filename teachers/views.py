from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from lms.utils import format_records
from webargs.djangoparser import use_args
from webargs import fields
from teachers import forms
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

    html_form = """
        <form method="get">
            <label for="first_name">First name:</label>
            <input type="text" id="fname" name="first_name"></br></br>

            <label for="last_name">Last name:</label>
            <input type="text" id="lname" name="last_name"></br></br>

            <label for="age">Age:</label>
            <input type="number" id="age" name="age"></br></br>

            <input type="submit" value="Submit">
        </form>
    """

    records = format_records(teachers)

    response = html_form + records

    return HttpResponse(response)


@csrf_exempt
def create_teacher(request):
    global form
    if request.method == 'GET':
        form = forms.TeachersCreateForm()
    elif request.method == 'POST':
        form = forms.TeachersCreateForm(data=request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/teachers/')

    html_form = f"""
                <form method="post">
                    {form.as_p()}
                    <input type="submit" value="Submit">
                </form>
                """
    return HttpResponse(html_form)
