# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, Http404, get_object_or_404, get_list_or_404
from .models import Author, Tag, Category, Post


# Create your views here.
def index(request):
    return HttpResponse("the D is Silent")

def post_list(request):
    posts = Post.objects.order_by("-id").all() #order by newest post first, oldest last
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', { 'post':post})

def posts_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), category=category)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/posts_by_category.html', context)

def posts_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/posts_by_tag.html', context)

def posts_by_author(request, author_slug):
    author = get_object_or_404(Author, slug=author_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), author=author)
    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'blog/posts_by_author.html', context)


def test_redirect(request):
    return redirect("/")

def test_cookie(request):
    if not request.COOKIES.get('color'):
        response = HttpResponse("Cookie Set")
        response.set_cookie('color', 'blue')
        return response
    else:
        return HttpResponse("Your favorite color is {0}".format(request.COOKIES['color']))

def track_user(request):
    response = render(request, 'blog/track_user.html')
    if not request.COOKIES.get('visits'):
        response.set_cookie('visits', '1', 3600*24*365*2)
    else:
        visits = int(request.COOKIES.get('visits',1)) +1
        response.set_cookie('visits', str(visits), 3600*24*365*2)
    return response

def stop_tracking(request):
    if request.COOKIES.get('visits'):
        response = HttpResponse("Cookies Cleared")
        response.delete_cookie("visits")
    else:
        reponse= HttpResponse("We are not tracking you.")
    return response

def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse("Testing session cookie")

def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Cookies can be set succesfully")
    else:
        response = HttpResponse("Cookies can not be set")
    return response