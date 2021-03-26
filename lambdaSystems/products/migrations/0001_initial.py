# Generated by Django 3.1.7 on 2021-03-26 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id_product', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('price', models.FloatField()),
                ('brand', models.CharField(max_length=120)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]
