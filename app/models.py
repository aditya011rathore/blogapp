from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	created_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	body = models.TextField()
	updated_at = models.DateTimeField(null=True, blank=True)
	class Meta:
		db_table="Post"
	def __str__(self):
		return self.title