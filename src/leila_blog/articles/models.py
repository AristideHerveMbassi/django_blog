from django.db import models
from django.contrib.auth.models import User
from categories.models import Categorie
from tags.models import Tag
from articles.help_text import *
from articles.verbose_name import *
# Create your models here.
STATUS_CHOICES = (
   ('draft', 'Draft'),
   ('published', 'Published'),
)


class Post(models.Model):
    author                  =       models.ForeignKey(User, on_delete=models.CASCADE)
    
    name                    =       models.CharField(max_length=100, unique=True, verbose_name=name_verbose_name, help_text=name_help_text)
    slug                    =       models.SlugField(max_length=100, null=False, blank=False, unique=True, editable=False)
    image                   =       models.FileField(null=False, blank=False, verbose_name=image_verbose_name, help_text=image_help_text)
    content                 =       models.TextField(max_length=255, verbose_name=content_verbose_name, help_text=content_help_text)
    like                    =       models.IntegerField(null=False, blank=False, editable=False)
    meta_description        =       models.TextField(max_length=255, verbose_name=meta_description_verbose_name, help_text=meta_description_help_text)
    created_at              =       models.DateField(auto_now=True,  editable=False)
    updated_at              =       models.DateField(auto_now=True,  editable=False)
    published_at              =       models.DateField(auto_now=False, editable=True)
    status                  =       models.CharField(max_length = 10, choices = STATUS_CHOICES, 
                                                      default ='draft')
    
    categories              =       models.ManyToManyField(Categorie, verbose_name=categories_verbose_name, help_text=categories_help_text)
    tags                    =       models.ManyToManyField(Tag, verbose_name=tags_verbose_name, help_text=tags_help_text)
    
    
    
    class Meta:
        ordering            =       ('-published_at',)

    def __str__(self):
        return self.name

    