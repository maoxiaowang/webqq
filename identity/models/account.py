from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.contrib.auth import models as auth_model


__all__ = [
    'User',
    'UserInfo',
    'UserActivity',
    'Group',
    'Permission'
]


class UserActivity(models.Model):
    """
    用户动作
    """
    user = models.ForeignKey('identity.User', models.CASCADE)
    type = models.CharField(max_length=32)

    class Meta:
        default_permissions = ()


class UserInfo(models.Model):
    """
    用户更多信息
    """
    GENDER_CHOICES = (
        ('male', _('male')),
        ('female', _('female')),
    )
    user = models.OneToOneField('identity.User', models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=11)

    class Meta:
        default_permissions = ()


class User(auth_model.AbstractUser):
    groups = models.ManyToManyField('identity.Group')
    user_permissions = models.ManyToManyField('identity.Permission')

    class Meta:
        db_table = 'auth_user'
        default_permissions = ()


class Group(auth_model.Group):

    class Meta:
        proxy = True


class Permission(auth_model.Permission):
    class Meta:
        proxy = True


models.DateTimeField(auto_now_add=True).contribute_to_class(auth_model.Group, 'created_at')
