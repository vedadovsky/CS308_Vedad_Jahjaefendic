from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class Books(models.Model):
    title = models.CharField(max_length=100, default='Default book title')
    authors = models.CharField(max_length=100, default='Default author')
    publisher = models.CharField(max_length=100,default='Default publisher')
    publication_date = models.DateTimeField(auto_now_add=True)
    number_of_pages = models.IntegerField(default=0)

    author = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        super(Books, self).save(*args, **kwargs)