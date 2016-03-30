from __future__ import unicode_literals

from django.db import models
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Name: ', max_length=100)
    location = forms.ChoiceField(label='Dojo Location: '
        ('sea', 'Seattle'),
        ('chi', 'Chicago'),
        ('dc', 'Washington DC'),
        ('sf', 'San Francisco'),
        ('ny', 'New York City'),
    )
    language = forms.ChoiceField(label='Favorite Language: '
        ('', ''),
        ('ruby', 'ruby'),
        ('python', 'python'),
        ('javascript', 'javascript'),
        ('c++', 'c++'),
        ('swift', 'swift'),
    )
    comment = forms.CharField(label='Comment: ')
