from django.shortcuts import render,get_object_or_404
from BlogPost.models import Post
from comment.models import Comments
from django.http import HttpResponse
from django.contrib.auth.views import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def ArticleDetail(request,articleId,articleSlug):
    if request.method == "GET":
        UserlikesMoreArticle = Post.objects.all().order_by("-users_like")[:5]
        UserReadsMoreArticle = Post.objects.all().order_by("-users_read")[:5]
        Article = get_object_or_404(Post,id=articleId)
        try:
            Article.users_read.add(request.user)
        except:
            pass
        Articles = Post.objects.filter(author=Article.author).order_by("-publish_time")[:10]
        Articles_Comment = Comments.objects.filter(Comment_article_id=articleId,Comment_parent=None,display=True)
        return render(request,"Article/detail.html",{"Article":Article,"Articles":Articles,"Comments":Articles_Comment,"Article_id":articleId
                                                     ,"ArticleSlug":articleSlug
                                                     ,"UserlikesMoreArticle":UserlikesMoreArticle,"UserReadsMoreArticle":UserReadsMoreArticle})
    if request.method == "POST":
        try:
            body = request.POST['body']
            IsNewComment = request.POST['IsNewComment']
            if IsNewComment == "False":
                ParentCommentId = request.POST['ParentCommentId']
            else:
                ParentCommentId = None
            comment = Comments()
            comment.body = body
            comment.user = request.user
            comment.Comment_parent_id = ParentCommentId
            comment.Comment_article_id = articleId
            comment.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")


@login_required(login_url="/account/login/")
@csrf_exempt
@require_POST
def like_article(request):

    ArticleId = request.POST.get("ArticleId")
    action = request.POST.get("action")
    if ArticleId and action:
        try:
            article = Post.objects.get(id=ArticleId)
            if action == "like":
                article.users_like.add(request.user)
                return HttpResponse("1")
            else:
                article.users_like.remove(request.user)
                return HttpResponse("2")
        except:
            return HttpResponse("no")