# Generated by Django 3.1.2 on 2021-02-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_comment_post_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_link',
            field=models.IntegerField(null=True),
        ),
    ]
