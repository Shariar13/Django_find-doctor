# Generated by Django 3.1.2 on 2021-10-04 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0040_auto_20211004_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='feed',
            new_name='feeds',
        ),
    ]
