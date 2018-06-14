from django.db import models
from datetime import datetime

#create the language model
class Language(models.Model):
    """Table for all languages"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    pubDate = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.CharField(max_length=255, blank=True)
    position = models.IntegerField(unique=True, blank=True)

    def __str__(self):
        return self.name

class Lists(models.Model):
    """ lists Table"""
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    language_name = language.name
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    pubDate = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.CharField(max_length=255, blank=True)
    position = models.IntegerField(unique=True, blank=True)

    def __str__(self):
        """name will returned in Admin panel"""
        return self.name

class Articles(models.Model):
    """ Articles Table """
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    article_list = models.ForeignKey(Lists, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    body = models.TextField()
    pubDate = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.CharField(max_length=255, blank=True)
    position = models.IntegerField(unique=True, blank=True)
    language_name = language.name
    list_name = article_list.name

    def __str__(self):
        return self.title