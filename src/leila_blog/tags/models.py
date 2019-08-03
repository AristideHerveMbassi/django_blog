from django.db import models
from tags.verbose_name import *
from tags.help_text import *

# Create your models here.
class Tag(models.Model):
    name            =        models.CharField(max_length=100, verbose_name=name_verbose_name, help_text=name_help_text, unique=True)
    description     =        models.TextField(max_length=255, verbose_name=description_verbose_name, help_text=description_help_text)
    created_at      =        models.DateField(auto_now=True)
    updated_at      =        models.DateField(auto_now=True)

    def __str__(self):
        return self.name
