# Generated by Django 3.1.2 on 2021-02-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20210204_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
