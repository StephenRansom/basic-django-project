# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Tag, Category, Post


# Create your views here.
def index(request):
    return HttpResponse("the D is Silent")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
