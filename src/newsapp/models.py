from django.db import models

class Article(models.Model):

    source_id = models.CharField(max_length=2048, null=True, blank=True)
    source_name = models.CharField(max_length=2048, null=True, blank=True)
    author = models.CharField(max_length=2048, null=True, blank=True)
    title = models.CharField(max_length=2048)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=2048, null=True, blank=True)
    url_to_image = models.URLField(max_length=2048, null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title 

