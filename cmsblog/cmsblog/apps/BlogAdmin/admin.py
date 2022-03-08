from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Users)
admin.site.register(Paymenttable)