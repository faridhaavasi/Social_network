from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(verbose_name='email Address', unique=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='User')
    id_name = models.CharField(max_length=50, unique=True, verbose_name='id')
    avatar = models.ImageField(upload_to='media/profile/avatar')
    bio = models.TextField()

    class Meta:
        ordering = ('user',)
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __str__(self):
        return f'{self.user.username}, {self.id_name}'

class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_ANDROID = 2
    DEVICE_IOS = 3
    DEVICE_PC = 4

    DEVICE_TYPE_CHOICES = (
        (DEVICE_WEB, 'web'),
        (DEVICE_ANDROID, 'android'),
        (DEVICE_IOS, 'ios'),
        (DEVICE_PC, 'pc')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    device_uuid = models.UUIDField('device UUID', null=True)
    last_login = models.DateTimeField('last login datetime', null=True)
    device_type = models.CharField(max_length=50, choices=DEVICE_TYPE_CHOICES, default=DEVICE_WEB)
    device_os = models.CharField('os device', max_length=20, blank=True)
    app_version = models.CharField('version_app', max_length=10, blank=True)
    device_model = models.CharField('device model', max_length=10, blank=True)

    class Meta:
        ordering = ('user', 'last_login')
        verbose_name = 'device'
        verbose_name_plural = 'devices'

    def __str__(self):
        return f'{self.user.username}={self.device_model}'
