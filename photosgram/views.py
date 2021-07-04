from django.http import HttpResponse
from datetime import datetime
import json


def hello_world(request):
    """Return the time"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Current server time is {now}')


def obj_request(request):
    # import pdb; pdb.set_trace()
    """Return a JSON response with sorted integers"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type="application/json"
    )


def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = f'Sorry {name}, you are not allowed here.'
    else:
        message = f'Hello, {name}! Welcome to Photosgram'
    
    return HttpResponse(message)