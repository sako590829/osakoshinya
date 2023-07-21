from django.db import models
from django.urls import reverse

class Blog(models.Model):
    createday = models.DateField()
    coment = models.CharField(max_length=200)
    image = models.ImageField(blank=True, default='nolmge.png')


    def __str__(self):
        return str(self.createday)
    
    def get_absolute_url(self):
        return reverse('list')

