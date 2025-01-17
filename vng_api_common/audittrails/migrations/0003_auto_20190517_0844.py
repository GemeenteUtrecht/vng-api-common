# Generated by Django 2.0.13 on 2019-05-17 08:44

import uuid

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audittrails', '0002_auto_20190516_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audittrail',
            name='aanmaakdatum',
            field=models.DateTimeField(auto_now=True, help_text='De datum waarop de handeling is gedaan'),
        ),
        migrations.AlterField(
            model_name='audittrail',
            name='actie',
            field=models.CharField(help_text='De uitgevoerde handeling', max_length=50),
        ),
        migrations.AlterField(
            model_name='audittrail',
            name='actie_weergave',
            field=models.CharField(blank=True, help_text='Vriendelijke naam van de actie', max_length=200),
        ),
        migrations.AlterField(
            model_name='audittrail',
            name='bron',
            field=models.CharField(help_text='De naam van het component waar de wijziging in is gedaan', max_length=50),
        ),
        migrations.AlterField(
            model_name='audittrail',
            name='hoofd_object',
            field=models.URLField(help_text='De URL naar het hoofdobject van een component', max_length=1000),
        ),
        migrations.AlterField(
            model_name='audittrail',
            name='nieuw',
            field=django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder, help_text='Volledige JSON body van het object na de actie', null=True),
        ),
        migrations.AlterField(
            model_name='audittrail',
            name='oud',
            field=django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder, help_text='Volledige JSON body van het object zoals dat bestond voordat de actie heeft plaatsgevonden', null=True),
        ),
        migrations.AlterField(
            model_name='audittrail',
            name='resource',
            field=models.CharField(help_text='Het type resource waarop de actie gebeurde', max_length=50),
        ),
        migrations.AlterField(
            model_name='audittrail',
            name='resource_url',
            field=models.URLField(help_text='De URL naar het object', max_length=1000),
        ),
        migrations.AlterField(
            model_name='audittrail',
            name='resultaat',
            field=models.IntegerField(help_text='HTTP status code van de API response van de uitgevoerde handeling'),
        ),
        migrations.AlterField(
            model_name='audittrail',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unieke identificatie van de audit regel', unique=True),
        ),
    ]
