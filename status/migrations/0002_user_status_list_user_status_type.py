# Generated by Django 3.1.7 on 2021-04-01 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_status_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='user_status_list',
            fields=[
                ('complaint_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.user_status_type')),
            ],
        ),
    ]
