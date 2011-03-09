from django.db import models

class Review(models.Model):
	review_id = models.IntegerField()
	user_id = models.IntegerField()
	beer_id = models.IntegerField()
	rating = models.IntegerField()
	review = models.CharField(max_length=1024)
	class Meta:
		db_table = u'reviews'
	def __unicode__(self):
        	return str(self.review_id)
