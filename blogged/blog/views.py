from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.
def Home(request):
    posts = Post.objects.all()

    return render(request, 'blog/index.html',{
        'posts': posts
    })

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/index.html',{
        'posts': post
    })
  