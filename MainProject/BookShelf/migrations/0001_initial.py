# Generated by Django 2.2.5 on 2020-02-17 16:55

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShelfItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('synopsis', models.CharField(max_length=300)),
            ],
            managers=[
                ('Shelfitems', django.db.models.manager.Manager()),
            ],
        ),
    ]
