from django.shortcuts import render
from django.conf import settings
from posts.models import Post
from django.views.generic import TemplateView

# Create your views here.
def index_view(request):
    posts = Post.objects.all()
    context = {
        "logo_pic": settings.MEDIA_URL + "cse_logo.png",
        "background_pic": settings.MEDIA_URL + "cse2.png",
        "posts": posts,  # Pass posts to the template
    }
    return render(request, "index.html", context)
