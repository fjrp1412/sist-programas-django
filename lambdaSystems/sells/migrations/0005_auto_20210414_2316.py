# Generated by Django 3.1.7 on 2021-04-14 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sells', '0004_sells_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sells',
            name='customer',
            field=models.CharField(default='None', max_length=20),
        ),
    ]