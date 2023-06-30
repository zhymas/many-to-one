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


















# class Musician(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     instrument = models.CharField(max_length=100)
#
#
# class Album(models.Model):
#     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     num_stars = models.IntegerField()


# class Person(models.Model):
#     SHIRT_SIZE = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     name = models.CharField(max_length=100)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)
    # p.get_shirt_size_display()

