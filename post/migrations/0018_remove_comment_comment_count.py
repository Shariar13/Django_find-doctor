# Generated by Django 3.1.2 on 2021-02-16 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_comment_comment_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_count',
        ),
    ]
