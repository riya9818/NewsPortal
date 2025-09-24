from django.contrib import admin
from newspaper.models import Category,Tag,Post,Advertisement, OurTeam, Contact, Comment, Newsletter
# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)
admin.site.register(OurTeam)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Newsletter)