from django.shortcuts import render,get_object_or_404
from BlogPost.models import Post
from comment.models import Comments
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def ArticleDetail(request,articleId,articleSlug):
    if request.method == "GET":
        Article = get_object_or_404(Post,id=articleId)
        Articles = Post.objects.filter(author=Article.author).order_by("-publish_time")[:10]
        Articles_Comment = Comments.objects.filter(Comment_article_id=articleId,Comment_parent=None,display=True)
        return render(request,"Article/detail.html",{"Article":Article,"Articles":Articles,"Comments":Articles_Comment,"Article_id":articleId
                                                     ,"ArticleSlug":articleSlug
                                                     })
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

