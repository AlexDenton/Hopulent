from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
	review_id = models.IntegerField(primary_key=True)
	user = models.ForeignKey(User)
	beer = models.ForeignKey('beer.Beer')
	rating = models.IntegerField()
	title = models.CharField(max_length=40)
	body = models.CharField(max_length=1024)
	class Meta:
		db_table = u'reviews'
	def __unicode__(self):
        	return str(self.review_id)
