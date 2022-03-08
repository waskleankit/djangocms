from django.urls import path
from cmsblog.apps.BlogAdmin import views

urlpatterns = [
    path('',views.blogadmin),
    path('adminboard/',views.adminboard),
    path('category/',views.category),
    path('adminpd/',views.adminpassword),
    path('deletebyadmin/<int:post_id>/',views.deletebyadmin , name="deletebyadmin"),
    path('add_category/',views.add_category),
    path('deletecategory/',views.deletecategory , name="deletecategory"),
    path('editcategory/',views.editcategory ),
]