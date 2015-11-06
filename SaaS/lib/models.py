from django.db import models

# Create your models here.
class Author(models.Model):
    ID = models.IntegerField(primary_key = True, max_length = 30)
    Name = models.CharField(max_length = 70)
    Age = models.IntegerField(max_length = 3)
    Country = models.CharField(max_length = 30)
    def __unicode__(self):
        return u'%s'%self.Name
class Book(models.Model):
    ISBN = models.IntegerField(max_length = 30, primary_key = True)
    Title = models.CharField(max_length = 30)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 30)
    PublishDate =  models.DateField()
    Price = models.DecimalField(decimal_places = 2,max_digits = 4)
    def __unicode__(self):
        return u'%s'% self.Title
    