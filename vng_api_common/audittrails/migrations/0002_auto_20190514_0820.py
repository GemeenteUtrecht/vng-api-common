# Generated by Django 2.0.13 on 2019-05-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audittrails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audittrail',
            name='applicatie_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='audittrail',
            name='applicatie_weergave',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
