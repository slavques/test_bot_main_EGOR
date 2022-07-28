# Generated by Django 4.0.6 on 2022-07-25 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usersmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='referral', serialize=False, to='usersmanage.user', unique=True, verbose_name='Пользователь'),
        ),
    ]