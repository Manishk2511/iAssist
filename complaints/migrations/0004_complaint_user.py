# Generated by Django 3.1.7 on 2021-03-23 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_latlong'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.IntegerField(default=0),
        ),
    ]
