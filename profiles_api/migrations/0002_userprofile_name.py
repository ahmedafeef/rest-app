# Generated by Django 3.2.20 on 2023-09-02 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
