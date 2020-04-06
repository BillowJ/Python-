from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.views.decorators.csrf import *
# Create your views here.

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.http import HttpResponse



def index(request):
    user_list = users.objects.all()
    user = request.COOKIES.get('user_name')


    paginator = Paginator(user_list, 5)
    page = request.GET.get('page', 1)
    currpage = int(page)

    try:

        user_list = paginator.page(page)
    except PageNotAnInteger:
        user_list = paginator.page(1)
    except EmptyPage:
        user_list = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'user' : user,
                                              'userlist' : user_list,'current_page':currpage,'page':page,'paginator':paginator})



def login(request):
    if request.method == 'POST':
        # print(request.POST)
        user = request.POST.get('user')
        password = request.POST.get('password')
        num = users.objects.filter(user_name=user, passwd=password).count()
        user_list = users.objects.all()
        if num:
            if users.objects.filter(user_name=user, passwd=password, admin=0):
                message = '用户权限不足！'
                return render(request, 'login.html', {'message' : message})
            rep = redirect('/index/')
            rep.set_cookie('user_name', user, 600)
            # rep.set_cookie('username', user, 60)
            # request.session['is_login'] = True
            # request.session['username'] = user
            return rep
        else:
            message = '用户不存在或密码错误！'
            return render(request, 'login.html', {'message': message,})
    return render(request, 'login.html')

def delete_user(request):

    user_name = request.GET.get('user_name')
    if users.objects.get(user_name=user_name):
        users.objects.get(user_name=user_name).delete()
    else:
        print('error')
    return redirect('/index')
@csrf_exempt
def adduser(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        admin = request.POST.get('admin')
        create_at = request.POST.get('date')
        user_id = request.POST.get('user_id')
        users.objects.create(user_name=user, passwd=password, create_at=create_at, admin = admin, user_id=user_id)
        return redirect('/index/')
        # user_list = users.objects.all()
    user = request.COOKIES.get('user_name')
    return render(request, 'adduser.html', {'user' : user})


@csrf_exempt
def modifyuser(request):
    if request.method == 'GET':
        userid = request.GET.get('user_id')
        default_user_name = request.GET.get('user')
        # obj = users.objects.filter(user_id=userid)
        return render(request, 'modifyuser.html', {'uid' : userid,
                                                   'user' : request.COOKIES.get('user_name'),
                                                   'default_user' : default_user_name})

    elif request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        admin = request.POST.get('admin')
        user_id = request.POST.get('user_id')
        users.objects.filter(user_id=user_id).update(user_name=user, passwd=password, admin=admin)
        rep = redirect('/index/')
        return rep

    user = request.COOKIES.get('user_name')
    return render(request, 'modifyuser.html', {'user' : user})


def blog(request):
    allblog = blogs.objects.all()
    user = request.COOKIES.get('user_name')

    paginator = Paginator(allblog, 6)
    page = request.GET.get('page', 1)
    currpage = int(page)

    try:

        allblog = paginator.page(page)
    except PageNotAnInteger:
        allblog = paginator.page(1)
    except EmptyPage:
        allblog = paginator.page(paginator.num_pages)

    return render(request, 'blogs.html', {'blogs' : allblog,
                                          'user' : user,'current_page':currpage,'page':page,'paginator':paginator}  )


def comment(request):
    commentlist = comments.objects.all()
    user = request.COOKIES.get('user_name')

    paginator = Paginator(commentlist, 4)
    page = request.GET.get('page', 1)
    currpage = int(page)

    try:

        commentlist = paginator.page(page)
    except PageNotAnInteger:
        commentlist = paginator.page(1)
    except EmptyPage:
        commentlist = paginator.page(paginator.num_pages)

    return render(request, 'comments.html', {'commentlist' : commentlist,
                                             'user' : user,'current_page':currpage,'page':page,'paginator':paginator})


def delete_comment(request):
    com_id = request.GET.get('com_id')
    if comments.objects.get(com_id = com_id):
        comments.objects.get(com_id=com_id).delete()
    else:
        print('error')
    return redirect('/comment')


def addcomment(request):
    if request.method == 'POST':
        com_id = request.POST.get('com_id')
        owner_id = request.POST.get('owner_id')
        blog_id = request.POST.get('blog_id')
        content = request.POST.get('content')
        create_at = request.POST.get('create_at')
        comments.objects.create(com_id=com_id, owner_id=owner_id, blog_id=blog_id, content=content, create_at=create_at)
        return redirect('/comment/')
    user = request.COOKIES.get('user_name')
    userlist = users.objects.all()
    bloglist = blogs.objects.all()
    return render(request, 'addcomment.html', {'user' : user,
                                               'userlist' : userlist,
                                               'bloglist' : bloglist})

def modifycomment(request):
    if request.method == 'GET':
        default_com_id = request.GET.get('com_id')
        # obj = users.objects.filter(user_id=userid)
        return render(request, 'modifycomment.html', {
                                                   'user' : request.COOKIES.get('user_name'),
                                                   'default_com_id' : default_com_id})

    if request.method == 'POST':
        com_id = request.POST.get('com_id')
        af_content = request.POST.get('content')
        comments.objects.filter(com_id=com_id).update(content=af_content)
        rep = redirect('/comment/')
        return rep


def addblog(request):
    if request.method == 'POST':
        owner_id = request.POST.get('owner_id')
        blog_id = request.POST.get('blog_id')
        content = request.POST.get('content')
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        create_at = request.POST.get('create_at')
        blogs.objects.create(owner_id=owner_id, title=title, summary=summary, blog_id=blog_id, content=content, created_at=create_at)
        return redirect('/blog/')
    userlist = users.objects.all()
    return render(request, 'addblog.html', {'user' : request.COOKIES.get('user'),
                                            'userlist' : userlist,})
@csrf_exempt
def search(request):
    if request.method == 'POST':
        id = request.POST.get('search')
        inf_user = users.objects.filter(user_id=id)
        # inf_com = comments.objects.filter(owner_id=id)
        inf_blog = blogs.objects.filter(owner_id=id).all()
        return render(request, 'search.html', {'user': request.COOKIES.get('user'),
                                               'bloglist' : inf_blog,
                                               'user_1' : inf_user})



def modifyblog(request):
    if request.method == 'GET':
        blog_id = request.GET.get('blog_id')
        default_content = request.GET.get('content')
        default_title = request.GET.get('title')
        default_summary = request.GET.get('summary')
        return render(request, 'modifyblog.html', {'user': request.COOKIES.get('user'),
                                                   'default_title': default_title,
                                                   'default_summary': default_summary,
                                                   'default_content': default_content,
                                                   'blog_id': blog_id,})
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        af_title = request.POST.get('title')
        af_content = request.POST.get('content')
        af_summary = request.POST.get('summary')
        blogs.objects.filter(blog_id=blog_id).update(title=af_title, content=af_content, summary=af_summary)
        rep = redirect('/blog/')
        return rep


