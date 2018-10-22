from django.conf.urls import url
from . import views as BlogPost_views

app_name = "BlogPost"

urlpatterns = [
    url(r'^PostManage/$',BlogPost_views.PostManage,name="PostManage"),
    url(r'^ColumnManage/$',BlogPost_views.ColumnManage,name="ColumnManage"),
    url(r'^ColumnEdit/$',BlogPost_views.ColumnEdit,name="ColumnEdit"),
    url(r'^ColumnDel/$',BlogPost_views.ColumnDel,name="ColumnDel"),
    url(r'^article-post/$',BlogPost_views.PostArticle,name="PostArticle"),
    url(r'^delete-post/$',BlogPost_views.delete_post,name="delete_post"),
    url(r'^Post_detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$',BlogPost_views.Post_detail,name="Post_detail"),
    url(r'^edit_post/(?P<post_id>\d+)/$',BlogPost_views.edit_post,name="edit_post"),
    url(r'^PersonalInformations/$',BlogPost_views.PersonalInformations,name="PersonalInformations"),
    url(r'^EditInformations/$',BlogPost_views.EditInformations,name="EditInformations"),

]