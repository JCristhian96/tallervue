from django.db import models
from django.db.models.signals import pre_save
# Signals
from . import signals


class Type(models.Model):
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description


class Category(models.Model):
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.description


class Element(models.Model):
    slug = models.SlugField(unique=True, editable=False)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description

# Signals
pre_save.connect(signals.set_slug, sender=Element)


