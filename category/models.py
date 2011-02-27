from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    cat_name = models.CharField(max_length=765)
    last_mod = models.DateTimeField()
    class Meta:
        db_table = u'categories'
    def __unicode__(self):
	return self.cat_name

