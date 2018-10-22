from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .forms import PostForm,ColumnForm
from .models import Post,Column
from account.models import Userprofile
from account.forms import UserprofileForm
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

@login_required(login_url='/account/login/')
@csrf_exempt
def ColumnManage(request):
    if request.method == "GET":
        columns = Column.objects.filter(user=request.user)
        column_form = ColumnForm()
        return render(request,"BlogPost/Column.html",{"columns":columns,"column_form":column_form})
    if request.method == "POST":
        column_name = request.POST['column']
        columns = Column.objects.filter(column=column_name)
        if columns:
            return HttpResponse("2")
        else:
            Column.objects.create(user=request.user,column=column_name)
            return HttpResponse("1")


@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def ColumnEdit(request):
    column_id = request.POST['column_id']
    column_name = request.POST['column_name']
    try:
        Line = Column.objects.get(id=column_id)
        Line.column = column_name
        Line.save()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def ColumnDel(request):
    column_id = request.POST['column_id']
    try:
        Line = Column.objects.get(id=column_id)
        Line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

@login_required(login_url='/account/login/')
def PostManage(request):
    Posts = Post.objects.filter(author=request.user)
    return render(request,"BlogPost/Post.html",{"Posts":Posts})

@login_required(login_url='/account/login/')
@csrf_exempt
def PostArticle(request):
    if request.method == "POST":
        article_post_form = PostForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = Column.objects.get(id=request.POST['column_id'])
                new_article.save()
                return HttpResponse("1")
            except:
                return  HttpResponse("2")
        else:
            return  HttpResponse("3")
    else:
        article_post_form = PostForm()
        article_columns = Column.objects.all()
        return render(request,"BlogPost/ArticlePost.html",{"article_post_form":article_post_form,"article_columns":article_columns})

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def delete_post(request):
    post_id = request.POST['post_id']
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

def Post_detail(request,id,slug):
    post = get_object_or_404(Post,id=id,slug=slug)
    return render(request,"BlogPost/PostDetail.html",{"post":post})

@login_required(login_url='/account/login')
@csrf_exempt
def edit_post(request,post_id):
    if request.method == "GET":
        columns = Column.objects.all()
        article = Post.objects.get(id=post_id)
        article_form = PostForm(initial={"title":article.title})
        this_article_column = article.column
        return render(request,"BlogPost/edit_post.html",{"columns":columns,"article":article,"article_form":article_form,"this_article_column":this_article_column})
    if request.method == "POST":
        article = Post.objects.get(id=post_id)
        try:
            column = request.POST['column']
            title = request.POST['title']
            body = request.POST['body']
            article.column = Column.objects.get(id=column)
            article.title = title
            article.body = body
            article.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")
@login_required(login_url='/account/login/')
@csrf_exempt
def PersonalInformations(request):
    userprofile = Userprofile.objects.get(user=request.user)
    Articles = Post.objects.filter(author=request.user)
    return render(request,"BlogPost/PersonalInformations.html",{"userprofile":userprofile,"Articles":Articles})

def EditInformations(request):
    if request.method == "GET":
        userprofile = Userprofile.objects.get(user=request.user)
        return render(request,"BlogPost/EditInformations.html",{"userprofile":userprofile})
    if request.method == "POST":
        try:
            motto = request.POST['motto']
            school = request.POST['school']
            phone = request.POST['phone']
            userprofile = Userprofile.objects.get(user=request.user)
            userprofile.motto = motto
            userprofile.School = school
            userprofile.phone = phone
            userprofile.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")