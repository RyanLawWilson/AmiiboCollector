# Generated by Django 2.2.5 on 2020-02-12 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Amiibo', '0006_auto_20200212_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amiibofigure',
            name='purchase_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]