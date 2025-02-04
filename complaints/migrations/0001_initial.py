# Generated by Django 3.1.7 on 2021-03-18 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image_upload',
            fields=[
                ('complaint_id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='otp_verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desciption', models.TextField()),
                ('area', models.CharField(max_length=110)),
                ('pincode', models.CharField(max_length=8)),
                ('image', models.ImageField(upload_to='img')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaints.problem')),
            ],
        ),
    ]
