from django.utils import timezone
from django.db import models

# Create your models here.

class TimeStampModel(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract= True # don't create table in DB

class Category(TimeStampModel):
    name = models.CharField(max_length=100)
    icon= models.CharField(max_length=100, null=True)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"] #order by gareko name a b c bata auxa
        verbose_name="category"
        verbose_name_plural="Categories"

class Tag(TimeStampModel):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(TimeStampModel):
    STATUS_CHOICES = [
        ("active","Active"),
        ("in_active","Inactive"),
    ]
    title=models.CharField(max_length=256)
    content=models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False) #install pillow library
    views_count= models.PositiveBigIntegerField(default=0)
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    is_breaking_news= models.BooleanField(default=False)
    published_at=models.DateTimeField(null=True, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    tags= models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Advertisement(TimeStampModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="advertisements/%Y/%m/%d", blank=False)

    def __str__(self):
        return self.title
    
class OurTeam(TimeStampModel):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team_images/%Y/%m/%d", blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title