
from django.shortcuts import render
from cmsblog.apps.BlogAdmin.models import *
from django.shortcuts import redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    page = request.GET.get('page', 1)
    try:
        email = request.user.email
        name = request.user
        # print(email)
        # print(name)
        # fname = request.firstname()
    except:
        name = None
        email = None
        # print(email)
        # print(email)
        # print(email)

    dbuser = Users.objects.filter(email=email).first()
    # print(dbuser)
    try:
        if str(name) != dbuser.name :
            # if str(name) != dbuser.name & str(name) != None:
            latest_user = Users.objects.latest('user_id')
            user_id=latest_user.user_id + 1
            password = "kuchbhi"
            role = "User"
            name = "{}".format(name)
            email = "{}".format(email)
            userinserting = Users(user_id,role,name,email,password)
            userinserting.save();
            name = request.user
            email = request.user.email
    except:
        print("exception inn double if ")

    if request.method == "POST":
        tag = request.POST['sv']
        posts = Posts.objects.filter(Q(description__contains=tag) | Q(title__contains=tag) | Q(date_created__contains=tag))
    else:
        postss = Posts.objects.order_by('-date_created')
        paginator = Paginator(postss,5)
        # print(page)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
    #     posts = Posts.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    user1 = Users.objects.filter(email=email).first()
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email,'posts':posts,'category' : cate,'username':username}
    return render(request,"fullwidth.html",context)


def home2(request,category_id):
    try:
        name = request.user
        email = request.user.email
    except:
        name = None
        email =None
    searchcat = category_id
    posts = Posts.objects.filter(category_id=searchcat)
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email,'posts':posts,'category' : cate,'username':username}
    return render(request,"fullwidth.html",context)