from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/300'
    },
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/300'
    },
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/300'
    },
]

# Create your views here.
def list_posts(request):
    """List existing posts"""
    return render(request, 'posts/feed.html', {'posts': posts})