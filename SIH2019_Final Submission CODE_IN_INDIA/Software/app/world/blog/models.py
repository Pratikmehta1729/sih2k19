from django.db import models


Create your models here.

class sampleemp(models.Model):
	PRODUCT_CODE = models.CharField(primary_key=True, max_length=50, null=False)
	TYRE_CODE = models.CharField(max_length=50, null=True)
	WEIGHT = models.FloatField(max_length=30, null=True)
	# VOLUME = models.FloatField(max_length=10, null=True)
	LOADING_TYPE = models.CharField(max_length=20, null=True)
	DIAMETER = modelswhile :
		pass.FloatField(max_length=30, null=True)

	
	class Meta:
		db_table = 'employee'





	
