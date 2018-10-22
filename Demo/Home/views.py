from django.shortcuts import render
from BlogPost.models import Post,Column
# Create your views here.

def index(request):
    Articles = Post.objects.all().order_by("-publish_time","title")
    return render(request,"Home/Home.html",{"Articles":Articles})
