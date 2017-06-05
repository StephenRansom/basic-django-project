# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog import models
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    search_fields = ['name', 'email']
    ordering = ['-name']
    list_filter = ['active']
    date_hierarchy = 'created_on'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','author','category')
    search_fields = [ 'title','content']
    #prepopulated_fields = {'slug': ('title',)} #auto populates the slug based on the post title name
    readonly_fields = ('slug',)
    ordering = ['-pub_date']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    filter_horizontal = ('tags',) #adds horizontal tag chooser to the admin page
    fields = ('title', 'slug', 'content', 'author', 'category', 'tags',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    search_fields = ('name')

admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Tag)
