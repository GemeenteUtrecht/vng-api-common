# Generated by Django 2.1.8 on 2019-05-06 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorizations', '0004_auto_20190503_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizationsconfig',
            name='component',
            field=models.CharField(choices=[('AC', 'Autorisatiecomponent'), ('NRC', 'Notificatierouteringcomponent'), ('ZRC', 'Zaakregistratiecomponent'), ('ZTC', 'Zaaktypecatalogus'), ('DRC', 'Documentregistratiecomponent'), ('BRC', 'Besluitregistratiecomponent')], default='ZRC', max_length=50, verbose_name='component'),
        ),
        migrations.AlterField(
            model_name='autorisatie',
            name='component',
            field=models.CharField(choices=[('AC', 'Autorisatiecomponent'), ('NRC', 'Notificatierouteringcomponent'), ('ZRC', 'Zaakregistratiecomponent'), ('ZTC', 'Zaaktypecatalogus'), ('DRC', 'Documentregistratiecomponent'), ('BRC', 'Besluitregistratiecomponent')], help_text='Name of the component to authorize', max_length=50),
        ),
    ]
