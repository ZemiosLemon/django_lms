from django.http import HttpResponse
from lms.utils import format_records
from teachers.models import Teachers
from webargs.djangoparser import use_args
from webargs import fields


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
