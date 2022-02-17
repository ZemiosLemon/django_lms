from django.http import HttpResponse
from lms.utils import format_records
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
    group = Group.objects.all()

    for key, value in args.items():
        if value:
            group = group.filter(**{key: value})

    html_form = """
        <form method="get">
            <label for="name_group">Group name:</label>
            <input type="text" id="name_group" name="name_group"></br></br>

            <label for="size_group">Size group:</label>
            <input type="number" id="size_group" name="size_group"></br></br>

            <input type="submit" value="Submit">
        </form>
    """

    records = format_records(group)

    response = html_form + records

    return HttpResponse(response)
