from django.contrib.auth import get_user_model
from django.db import models
from django.apps import apps

# Create your models here.

User = get_user_model()


class Post(models.Model):
    content = models.TextField(max_length=1024)
    user = models.ForeignKey(User, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        default_permissions = ()
