from django.shortcuts import render,get_object_or_404
from BlogPost.models import Post
# Create your views here.

def ArticleDetail(request,articleId,articleSlug):
    Article = get_object_or_404(Post,id=articleId)
    Articles = Post.objects.filter(author=Article.author).order_by("-publish_time")[:10]
    return render(request,"Article/detail.html",{"Article":Article,"Articles":Articles})