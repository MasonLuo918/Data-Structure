from django.conf.urls import url
from . import views as comment_views
app_name = "comment"
urlpatterns = [
    url(r'^comment_test/(?P<ArticleId>\d+)/$',comment_views.CommentFunction,name="CommentFunction"),
]