from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class QRCode(models.Model):
	TYPE_CHOICES = (
		('e', 'Email'),
		('w', 'Website'),
		('t', 'Twitter'),
		('s', 'Text'),
	)

	user = models.ForeignKey(User, null=True, blank=True)
	link_id = models.CharField(max_length=50)
	size = models.CharField(max_length=1, default='l')
	type = models.CharField(max_length=1, default='t', choices=TYPE_CHOICES)
	text = models.TextField()
	name = models.CharField(max_length=100, default='')
	phone_number = models.CharField(max_length=25, default='')
	email = models.CharField(max_length=100, default='')
	url = models.URLField(verify_exists=True, max_length=200)
	company = models.CharField(max_length=100, default='')
	pub_date = models.DateTimeField(default=datetime.now())