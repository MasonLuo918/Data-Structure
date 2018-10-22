"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Home import views as Home_views
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^account/',include("account.urls")),
    url(r'^pwd_reset/',include("password_reset.urls",namespace="pwd_reset",app_name="pwd_reset")),
    url(r'^BlogPost/',include("BlogPost.urls")),# import the BlogPost app
    url(r'^home/',Home_views.index,name="index"),
    url(r'^Article/',include("Articleapp.urls",namespace="Articleapp",app_name="Articleapp")),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
