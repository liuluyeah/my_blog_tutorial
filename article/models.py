# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100)  #bolg name
    category = models.CharField(max_length = 50, blank = True) #bolg title
    date_time = models.DateTimeField(auto_now_add = True) #blog time
    content = models.TextField(blank = True, null = True) #blog text

    def _str_(self):
        return self.title

    class Meta:
        ordering = ['-date_time']

# Create your models here.
