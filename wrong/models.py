from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.


class Occurrence(models.Model):
    TimeWrong = models.IntegerField(verbose_name='How Long Was Gerald Wrong (In Minutes)')
    Subject = models.CharField(max_length=100, verbose_name='Enter The Topic Gerald Was Wrong About')
    Details = models.CharField(max_length=500)
    DateTime = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.Subject + ' ' + str(self.DateTime)

    def get_absolute_url(self):
        return reverse('wrong:wrong-detail', kwargs={'pk': self.pk})


