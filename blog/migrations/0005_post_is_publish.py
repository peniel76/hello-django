# Generated by Django 2.1.5 on 2019-02-18 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190218_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_publish',
            field=models.BooleanField(default=False),
        ),
    ]
