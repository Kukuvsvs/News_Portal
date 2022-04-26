from django.db import models
from django.shortcuts import reverse

# Create your models here.
class New(models.Model):
    objects = None
    title = models.CharField(max_length=64)
    Text = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128, unique=True)

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug':self.slug} )

    def __str__(self):
        return '{}'.format(self.title)