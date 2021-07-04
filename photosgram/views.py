from django.http import HttpResponse
from datetime import datetime


def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Current server time is {now}')


def obj_request(request):
    import pdb; pdb.set_trace()
    return HttpResponse('Hello!')