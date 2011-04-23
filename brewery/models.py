from django.db import models

class Brewery(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    address1 = models.CharField(max_length=765)
    address2 = models.CharField(max_length=765, blank=True)
    city = models.CharField(max_length=765)
    state = models.CharField(max_length=765)
    code = models.CharField(max_length=75)
    country = models.CharField(max_length=765)
    phone = models.CharField(max_length=150, blank=True)
    website = models.CharField(max_length=765, blank=True)
    filepath = models.CharField(max_length=765, blank=True)
    descript = models.TextField(blank=True)
    add_user = models.IntegerField()
    last_mod = models.DateTimeField()
    class Meta:
        db_table = u'breweries'
    def __unicode__(self):
	   return self.name
