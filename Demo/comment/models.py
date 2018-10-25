from django.db import models
from BlogPost.models import Post
from django.contrib.auth.models import User
# Create your models here.
class Comments(models.Model):
    body = models.TextField() #评论体
    user = models.ForeignKey(User,related_name="Comment")
    Comment_parent = models.ForeignKey('self',related_name="child_comment",null=True,blank=True)
    Comment_article = models.ForeignKey(Post,related_name="comments")
    comment_time = models.DateTimeField(auto_now_add=True,null=True)
    display = models.BooleanField(default=True)

    class Meta:
        ordering = ("-comment_time",)

    def __str__(self):
        return "{0}-{1}".format(self.user.username,self.id)