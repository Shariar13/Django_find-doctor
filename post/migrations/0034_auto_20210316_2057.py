# Generated by Django 3.1.2 on 2021-03-16 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0033_auto_20210316_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='name',
            new_name='feedbacker_name',
        ),
    ]
