# Generated by Django 4.2.3 on 2023-07-24 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment_reply_like_comment_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_comment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_like', to='posts.comment'),
        ),
    ]
