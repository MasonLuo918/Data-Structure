from django.shortcuts import render,get_object_or_404
from BlogPost.models import Post,Column
from account.models import Userprofile
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def index(request):
    Articles = Post.objects.all().order_by("-publish_time","title")
    paginator = Paginator(Articles,8)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    return render(request,"Home/Home.html",{"Articles":articles,"page":current_page})
