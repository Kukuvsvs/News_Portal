from django.db import models
from django.shortcuts import reverse
from django.views.generic.list import ListView

# Create your models here.
class New(models.Model, ListView):
    objects = None
    title = models.CharField(max_length=64)
    Text = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=128, unique=True)
    ordering = 'date_pub'

    def get_absolute_url(self):
        return reverse('details', kwargs={'slug':self.slug} )

    def __str__(self):
        return '{}'.format(self.title),