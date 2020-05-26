from django.db import models

class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE,)
    title = models.CharField(max_length = 100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.title
