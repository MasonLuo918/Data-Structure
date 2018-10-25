from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import Userprofile,EmailVerifyRecord
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from BlogPost.models import Post
from django.contrib.auth.models import User
from utils.email_send import send_register_email
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
# Create your views here.

def register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            user = user_form.save(commit=False)
            user.is_active = False
            user.set_password(password)
            user.save()
            userprofile = Userprofile(user=user)
            userprofile.save()
            send_register_email(email)
            return render(request,"account/Success.html")
    else:
        user_form = RegisterForm()
    return render(request,"account/register.html",{"user_form":user_form})

def ActivateUser(request,activate_code):
    print(activate_code)
    all_records = EmailVerifyRecord.objects.filter(code=activate_code)
    if all_records:
        for record in all_records:
            email = record.email
            user = User.objects.get(email=email)
            user.is_active=True
            user.save()
    else:
        return render(request,"account/active_fail.html")
    return render(request,"account/activate.html")

@login_required(login_url="/account/login/")
def AuthorArticle(request,user_id):
    Articles = Post.objects.all().order_by("-publish_time")
    paginator = Paginator(Articles,8)
    page = request.GET.get("page")
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    userprofile = get_object_or_404(Userprofile,id=user_id)
    return render(request,"account/AuthorArticle.html",{"Articles":articles,"userprofile":userprofile})
