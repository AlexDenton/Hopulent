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
