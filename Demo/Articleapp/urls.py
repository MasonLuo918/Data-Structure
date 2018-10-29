from django.conf.urls import url
from . import views as Article_views

urlpatterns = [
    url(r'^ArticleDetail/(?P<articleId>\d+)/(?P<articleSlug>[-\w]+)/$',Article_views.ArticleDetail,name="ArticleDetail"),
    url(r'^LikeArticle/$',Article_views.like_article,name="like_article"),
]