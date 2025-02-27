from django.shortcuts import render
from django.conf import settings
from posts.models import Post
from django.views.generic import TemplateView

class PostListTemplate(TemplateView):
  template_name="index.html"
  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    post_data=Post.objects.all()
    context["data"]=post_data
    return context

# Create your views here.
def index_view(request):
    posts = Post.objects.all()
    context = {
        "logo_pic": settings.MEDIA_URL + "cse_logo.png",
        "background_pic": settings.MEDIA_URL + "cse2.png",
        "posts": posts,  # Pass posts to the template
    }
    return render(request, "index.html", context)
def home_view(request):
    context = {
        'professor_pic': settings.MEDIA_URL + 'chairman.png',  # Update filename if different
    }
    return render(request, 'home.html', context)