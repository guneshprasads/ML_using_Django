# Generated by Django 3.1 on 2020-08-22 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Openml', '0003_auto_20200822_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csv',
            old_name='csvname',
            new_name='name',
        ),
    ]