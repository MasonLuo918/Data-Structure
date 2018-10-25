from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from slugify import slugify
# Create your models here.

class Column(models.Model):
    column = models.CharField(max_length=30)
    user = models.ForeignKey(User,related_name="user_column")
    created_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column


class Post(models.Model):

    title = models.CharField(max_length=40)
    body = models.TextField()
    author = models.ForeignKey(User,related_name="UserPost")
    column = models.ForeignKey(Column,related_name="Pospt_Column",default='')
    abstract = models.CharField(max_length=200,null=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=500,blank=True)

    def __str__(self):
        return "%s-%s" % (self.author.username,self.title)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        self.abstract = "  "  + self.body[:190]
        self.abstract += ".."
        super(Post,self).save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse("BlogPost:Post_detail",args=[self.id,self.slug])

    def get_detail_url(self):
        return reverse("Articleapp:ArticleDetail",args=[self.id,self.slug])

    class Meta:
        ordering = ("-publish_time","title")
        index_together = (("id","slug"),)

