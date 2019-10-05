from django.db import models
# from django.db.models.signals import pre_save
from django.utils.text import slugify
import datetime


class Majmu(models.Model):
    name = models.CharField(max_length=255)
    page = models.IntegerField()
    slug = models.SlugField(max_length = 255, null = True, blank = True)
    date = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return str(self.slug)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Majmu, self).save(*args, **kwargs)
 