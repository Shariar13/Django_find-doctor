# Generated by Django 3.1.2 on 2021-02-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_author_name',
            field=models.CharField(max_length=99, null=True),
        ),
    ]