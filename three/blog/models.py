# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique = True)
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField()
    last_logged_in = models.DateTimeField()
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
class Post(models.Model):
    title = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    