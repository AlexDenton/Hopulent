from django.db import models

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
