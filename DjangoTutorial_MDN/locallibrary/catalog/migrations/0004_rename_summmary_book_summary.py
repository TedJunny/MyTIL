# Generated by Django 3.2.6 on 2021-08-16 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210812_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='summmary',
            new_name='summary',
        ),
    ]