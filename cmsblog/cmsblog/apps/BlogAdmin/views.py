from django.shortcuts import render , redirect
from django.http import HttpResponse
from cmsblog.apps.BlogAdmin.models import *
from django.utils import timezone
# Create your views here.

def blogadmin(request):
    return render(request,'BlogAdmin/adminlogin.html')


def adminpassword(request):
    name = request.POST["loginid"]
    password = request.POST["pd"]
    blogadmin = Users.objects.filter(role="admin").first()
    username=blogadmin.name
    userpassword=blogadmin.password
    if name == username and password == userpassword:
        posts = Posts.objects.order_by('-date_created')
        cate = Category.objects.all()
        username = Users.objects.all()
        context = {'posts':posts,'category' : cate,'username' : username ,'blogadmin':blogadmin}
        return render(request,'BlogAdmin/admindashboard.html',context)
    else:
        message="Enter correct userid and password"
        context = {'message': message}
        return render(request, 'BlogAdmin/adminlogin.html',context)


def adminboard(request):
    posts = Posts.objects.order_by('-date_created')
    cate = Category.objects.all()
    username = Users.objects.all()
    blogadmin = Users.objects.filter(role="admin").first()
    context = {'posts':posts,'category' : cate,'username' : username ,'blogadmin':blogadmin}
    return render(request,'BlogAdmin/admindashboard.html',context)


from django.shortcuts import get_object_or_404
def deletebyadmin(request,post_id):
    posts = get_object_or_404(Posts, pk=post_id).delete()
    return redirect('/blogadmin/adminboard')


def category(request):
    cate = Category.objects.all()
    blogadmin = Users.objects.filter(role="admin").first()
    context = {"category":cate,'blogadmin':blogadmin}
    return render(request, 'BlogAdmin/categories.html',context)


def add_category(request):
    category_name = request.POST['name']

    create_date = timezone.now()
    update_date = timezone.now()
    latest_category = Category.objects.latest('category_id')
    categoryid=latest_category.category_id + 1
    cat=Category(categoryid,category_name,create_date,update_date)
    cat.save()
    return redirect('/blogadmin/category')


def deletecategory(request):
    idvalue = request.POST['a']
    print(idvalue)
    Category.objects.filter(category_id = idvalue).delete()
    return redirect('/blogadmin/category')


def editcategory(request):
    update_date = datetime.utcnow()
    name=request.POST['upda']
    cate = Category.objects.filter(category_id = request.POST['b']).first()
    cate.category_name = name
    cate.save()
    return redirect('/blogadmin/category')

