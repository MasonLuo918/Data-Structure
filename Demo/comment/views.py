from django.shortcuts import render,get_object_or_404
from .models import Comments
from django.http import HttpResponse
from BlogPost.models import Post
import re
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
    array = (r'习*平',r'李*强',r'尼玛',r'你妈',r'他妈',r'我曹',r'握草',r'窝草',r'我操',r'卧槽',r'傻逼',r'煞笔',r'麻痹',r'马蛋',r'鸡巴',r'我日',r'滚蛋',r'去他妈')
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
