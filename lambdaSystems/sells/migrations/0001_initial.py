# Generated by Django 3.1.7 on 2021-03-29 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sells',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=120)),
                ('products', models.JSONField()),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('id_salesman', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.salesman')),
            ],
        ),
    ]
