from django.db import models
import random
import string
from jsonfield import JSONField

class Appraisement(models.Model):
	code = models.TextField(null=False, max_length=8, unique=True)
	parsed_items = JSONField(default={})
	bad_lines = JSONField(default={})
	prices = JSONField(default={})
	representative_kind = models.TextField(default='unknown')
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="created date")


	def __str__(self):
		return self.code

	def save(self, *args, **kwargs):
		if self.pk is None:
			self.generate_code(8)
		super(Appraisement, self).save(*args, **kwargs)

	def generate_code(self, url_len):
		caract = string.ascii_letters + string.digits
		self.code = ''.join([random.choice(caract) for _ in range(url_len)])