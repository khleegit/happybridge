from django.db import models

# Create your models here.
class Affiliatedstore(models.Model):
	receipt_date = models.DateField(auto_now = False)
	receipt_staff = models.CharField(max_length = 20)
	brand = models.CharField(max_length = 30)
	affiliated_store = models.CharField(max_length = 40)
	item_number = models.CharField(max_length = 20)
	item = models.CharField(max_length = 50)
	classification = models.CharField(max_length = 20)
	receipt_contents = models.TextField()
	answer_staff = models.CharField(max_length = 20)
	answer_contents = models.TextField()
	answer_date = models.DateField(auto_now = False)
	note = models.TextField()

	def __str__(self):
		return self.receipt_date


class Consumer(models.Model):
	receipt_date = models.DateField(auto_now = False)
	receipt_staff = models.CharField(max_length = 20)
	brand = models.CharField(max_length = 30)
	supervisor = models.CharField(max_length = 40)
	affiliated_store = models.CharField(max_length = 40)
	receipt_channel = models.CharField(max_length = 30)
	classification = models.CharField(max_length = 20)
	receipt_contents = models.TextField()
	answer_staff = models.CharField(max_length = 20)
	answer_contents = models.TextField()
	answer_date = models.DateField(auto_now = False)
	note = models.TextField()

	def __str__(self):
		return self.receipt_date


class Delivery(models.Model):
	bp_code = models.CharField(max_length = 50)
	sunday = models.CharField(max_length = 6)
	monday = models.CharField(max_length = 6)
	tuesday = models.CharField(max_length = 6)
	wednesday = models.CharField(max_length = 6)
	thursday = models.CharField(max_length = 6)
	friday = models.CharField(max_length = 6)
	saturday = models.CharField(max_length = 6)
	center = models.CharField(max_length = 20)

	def __str__(self):
		return self.bp_code