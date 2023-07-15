from django.db import models
from account.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Users')
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='media/pos')
    caption = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=True)
    class Meta:
        ordering = ('user', 'created')
        verbose_name = 'post'
        verbose_name_plural = 'posts'


    def __str__(self):
        return f'{self.user}-{self.title}'

