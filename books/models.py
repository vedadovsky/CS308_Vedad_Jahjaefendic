from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class Books(models.Model):
    title = models.CharField(max_length=100, default='Default book title')
    authors = models.CharField(max_length=100, default='Default author')
    publisher = models.CharField(max_length=100,default='Default publisher')
    publication_date = models.DateTimeField(auto_now_add=True)
    number_of_pages = models.IntegerField(default=0)
