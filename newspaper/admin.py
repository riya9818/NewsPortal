from django.contrib import admin
from newspaper.models import Category,Tag,Post,Advertisement
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)