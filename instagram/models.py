from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, editable=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False, db_index=True)
    ip = models.GenericIPAddressField(null=True, editable=False)