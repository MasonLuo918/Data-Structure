from django.shortcuts import render,get_object_or_404
from .models import Comments
from django.http import HttpResponse
from BlogPost.models import Post
# Create your views here.
# class Comments(models.Model):
#     body = models.TextField() #评论体
#     user = models.ForeignKey(User,related_name="Comment")
#     Comment_parent = models.ForeignKey('self',related_name="child_comment")
#     Comment_article = models.ForeignKey(Post,related_name="comments")
#
#     def __str__(self):
#         return "{}".format(self.user.username)

def CommentFunction(request,ArticleId):
    if request.method == 'GET':
        Comment_List = Comments.objects.filter(Comment_article=ArticleId)
        CommentsList = []
        for item in Comment_List:
            if item.Comment_parent == None:
                CommentsList.append(item)
        return render(request,"comment/MyselfComment.html",{"CommentsList":CommentsList,"ArticleId":ArticleId})
    if request.method == "POST":
        try:
            HasParent = request.POST["HasParent"]
            ParentId = request.POST["ParentId"]
            body = request.POST["body"]
            user = request.user
            if HasParent == "False":
                new_comment = Comments()
                new_comment.body = body
                # print("*********")
                new_comment.save()
            else:
                new_comment = Comments()
                new_comment.body = body
                print("*********")
                new_comment.user = user
                print("************")
                new_comment.Comment_article_id = ArticleId
                new_comment.Comment_parent_id = ParentId
                print("***********")
                new_comment.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")
