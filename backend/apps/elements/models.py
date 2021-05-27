from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Type(models.Model):
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description


class Category(models.Model):
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description


class Element(models.Model):
    slug = models.SlugField(
        unique=True,
        blank=False,
        null=True,
        editable=False

    )
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description


def set_slug(instance, sender, *args, **kwargs):
    instance.slug = slugify(instance.description)
    
    return instance

pre_save.connect(set_slug, sender=Element)


