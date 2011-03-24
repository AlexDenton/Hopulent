from django.db import models
from brewery.models import Brewery
from category.models import Category
from style.models import Style
class Beer(models.Model):
    id = models.IntegerField(primary_key=True)
    brewery = models.ForeignKey(Brewery)
    name = models.CharField(max_length=765)
    cat = models.ForeignKey(Category)
    style = models.ForeignKey(Style)
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
