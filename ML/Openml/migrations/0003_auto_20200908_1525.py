# Generated by Django 3.1 on 2020-09-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Openml', '0002_matrixvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrixvalue',
            name='x',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='matrixvalue',
            name='y',
            field=models.IntegerField(),
        ),
    ]
