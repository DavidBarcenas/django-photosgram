from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/300'
    },
    {
        'name': 'Mont Blac',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/300'
    },
    {
        'name': 'Mont Blac',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/300'
    },
]

# Create your views here.
def list_posts(request):
    """List existing posts"""
    content = []

    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <img src="{picture}"/>
        """.format(**post))

    return HttpResponse('<br />'.join(content))
