from django.db import models

# Create your models here.


class News(models.Model):
    author = models.CharField(max_length=250, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    urlToImage = models.CharField(max_length=500, null=True, blank=True)
    publishedAt = models.DateTimeField()
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return "title| {} ".format(self.title)
