# Generated by Django 3.2.5 on 2022-01-06 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['id', 'pk', 'c'], 'verbose_name': 'products', 'verbose_name_plural': 'products'},
        ),
    ]