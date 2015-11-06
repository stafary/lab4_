# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:10:52 2015

@author: huanhuan
"""
from django import forms
class Sys(forms.Form):
    query = forms.CharField(max_length = 50,label = "Input an author\'s name:")
class newBook(forms.Form):
    ISBN = forms.IntegerField()
    Title = forms.CharField(max_length = 30)
    Author = forms.CharField(max_length = 30)
    Publisher = forms.CharField(max_length = 30)
    PublishDate =  forms.DateField()
    Price = forms.DecimalField(decimal_places = 2,max_digits = 4)
class newBook2(forms.Form):
    Author = forms.CharField(max_length = 30)
    Publisher = forms.CharField(max_length = 30)
    PublishDate =  forms.DateField()
    Price = forms.DecimalField(decimal_places = 2,max_digits = 4)
class newAuthor(forms.Form):
    ID = forms.IntegerField()
    Name = forms.CharField(max_length = 70)
    Age = forms.IntegerField()
    Country = forms.CharField(max_length = 30)