# Generated by Django 2.1.5 on 2019-05-29 14:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ikp_sis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
