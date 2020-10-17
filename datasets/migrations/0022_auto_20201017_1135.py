# Generated by Django 3.1.1 on 2020-10-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0021_historicalcitycouncilattendancelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citycouncilrevenue',
            name='external_code',
            field=models.PositiveIntegerField(db_index=True, unique=True, verbose_name='Código externo'),
        ),
    ]
