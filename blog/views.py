from django.shortcuts import render

posts = [
    {
        'author': 'Anirudh Kanabar',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'October 25, 2021'
    },
    {
        'author': 'Anirudh Kanabar',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'October 25, 2021'
    }
]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
