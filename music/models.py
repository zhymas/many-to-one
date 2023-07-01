from django.db import models
from django.urls import reverse


class Reporter(models.Model):
    firs_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.firs_name, self.last_name)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']




















