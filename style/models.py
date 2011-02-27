from django.db import models

class Style(models.Model):
    id = models.IntegerField(primary_key=True)
    cat_id = models.IntegerField()
    style_name = models.CharField(max_length=765)
    last_mod = models.DateTimeField()
    class Meta:
        db_table = u'styles'
    def __unicode__(self):
	return self.style_name
