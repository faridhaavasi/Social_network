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

    def __str__(self):
        return f'{self.user}-{self.title}'

    class Meta:
        ordering = ('user', 'created')
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='posts')
    text = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.post}-{self.created}'

    class Meta:
        ordering = ('post', 'created')
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.comment}-{self.created}'

    class Meta:
        ordering = ('comment', 'created')
        verbose_name = 'reply'
        verbose_name_plural = 'replys'


class Like(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='post')
    like = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post}-{self.created}'

    class Meta:
        ordering = ('post', 'created')
        verbose_name = 'like'
        verbose_name_plural = 'likes'


class Like_comment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments_like')
    like = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment}-{self.created}'

    class Meta:
        ordering = ('comment', 'created')
        verbose_name = 'like_comment'
        verbose_name_plural = 'like_comments'
