from django.db import models
from django.db.models import Model
# Create your models here.
from datetime import datetime
from django.utils import timezone

# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.db import models
# from oauth2client.contrib.django_util.models import CredentialsField



class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date_created = models.DateTimeField('date published',default=timezone.now())
    category_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', blank=True,null =True)
    def __str__(self):
        return "{0} , {1} , {2} , {3}, {4}, {5} , {6}".format(self.id,self.title,self.description,self.date_created,self.category_id,self.user_id, self.image)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=50)
    create_date = models.DateTimeField('date published',default=timezone.now())
    update_date = models.DateTimeField('date updated',default=timezone.now())
    def __str__(self):
        return "{0} , {1} , {2} , {3}".format(self.category_id,self.category_name,self.create_date,self.update_date)

class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=50,default="user")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    def __str__(self):
        return "{0} , {1} , {2} , {3}, {4}".format(self.user_id,self.role,self.name,self.email,self.password)


class Paymenttable(models.Model):
    payment_id = models.IntegerField(max_length=50,primary_key=True)
    user_id = models.IntegerField(default=2)
    payer_id = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    email = models.EmailField()
    name = models.CharField(max_length=50)
    json_response = models.CharField(max_length=50)
    def __str__(self):
        return "{0} , {1} , {2} , {3}, {4}, {5} , {6}".format(self.payment_id, self.user_id,self.payer_id,self.amount, self.email, self.name,self.json_response)





# class CredentialsModel(models.Model):
#     id = models.ForeignKey(User, primary_key = True, on_delete = models.CASCADE)
#     credential = CredentialsField()
#     task = models.CharField(max_length = 80, null = True)
#     updated_time = models.CharField(max_length = 80, null = True)
#
#
# class CredentialsAdmin(admin.ModelAdmin):
#     pass





# class Customer(models.Model):
#     id = models.IntegerField(default=0,primary_key=True)
#     name = models.CharField(max_length=50)
#     gender = models.CharField(max_length=10)
#     account_type = models.CharField(max_length=10)
#     balance = models.IntegerField(default=0)
#     account_no = models.IntegerField(default=0)
#     pub_date = models.DateTimeField('date published',default=timezone.now())
#
#     def __str__(self):
#         return "{0} , {1} , AccNo-{2} , Balance-{3}".format(self.name,self.gender,self.account_no,self.balance)





#    user_id integer NOT NULL,
#     role character varying COLLATE pg_catalog."default" DEFAULT USER,
#     name character varying COLLATE pg_catalog."default",
#     email character varying COLLATE pg_catalog."default",
#     password character varying COLLATE pg_catalog."default",
#     CONSTRAINT "Users_pkey" PRIMARY KEY (user_id)
#     def __repr__(self):
#         return '<User %r>' % self.id