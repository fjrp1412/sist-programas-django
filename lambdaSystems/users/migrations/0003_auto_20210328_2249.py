# Generated by Django 3.1.7 on 2021-03-28 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210328_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='id',
        ),
        migrations.AddField(
            model_name='admin',
            name='admin_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
