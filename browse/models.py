# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models



class Beer(models.Model):
    id = models.IntegerField(primary_key=True)
    brewery_id = models.IntegerField()
    name = models.CharField(max_length=765)
    cat_id = models.IntegerField()
    style_id = models.IntegerField()
    abv = models.FloatField()
    ibu = models.FloatField()
    srm = models.FloatField()
    upc = models.IntegerField()
    filepath = models.CharField(max_length=765)
    descript = models.TextField()
    add_user = models.IntegerField()
    last_mod = models.DateTimeField()
    class Meta:
        db_table = u'beers'
    def __unicode__(self):
        return self.name

class Brewer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    address1 = models.CharField(max_length=765)
    address2 = models.CharField(max_length=765)
    city = models.CharField(max_length=765)
    state = models.CharField(max_length=765)
    code = models.CharField(max_length=75)
    country = models.CharField(max_length=765)
    phone = models.CharField(max_length=150)
    website = models.CharField(max_length=765)
    filepath = models.CharField(max_length=765)
    descript = models.TextField()
    add_user = models.IntegerField()
    last_mod = models.DateTimeField()
    class Meta:
        db_table = u'breweries'
    def __unicode__(self):
        return self.name


class BreweriesGeocode(models.Model):
    id = models.IntegerField(primary_key=True)
    brewery_id = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy = models.CharField(max_length=765)
    class Meta:
        db_table = u'breweries_geocode'
    def __unicode__(self):
        return self.accuracy

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=765)
    last_mod = models.DateTimeField()
    class Meta:
        db_table = u'categories'
    def __unicode__(self):
        return self.cat_name


class Style(models.Model):
    id = models.IntegerField(primary_key=True)
    cat_id = models.IntegerField()
    style_name = models.CharField(max_length=765)
    last_mod = models.DateTimeField()
    class Meta:
        db_table = u'styles'
    def __unicode__(self):
        return self.style_name


