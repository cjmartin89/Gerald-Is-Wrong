from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.


class Quotes(models.Model):
    Quote = models.CharField(max_length=999)
    Person = models.CharField(max_length=999, verbose_name='Who said it ?')
    DateTime = models.DateField(default=timezone.now(), verbose_name='Date: ')

    def __str__(self):
        return self.Subject

    def get_absolute_url(self):
        return reverse('quotes:quote-detail', kwargs={'pk': self.pk})
