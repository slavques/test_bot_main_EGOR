# Generated by Django 4.0.6 on 2022-07-22 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Название Товара')),
                ('photo', models.CharField(max_length=200, verbose_name='Фото file_id')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
                ('description', models.TextField(max_length=3000, null=True, verbose_name='Описание')),
                ('category_code', models.CharField(max_length=20, verbose_name='Код категории')),
                ('category_name', models.CharField(max_length=20, verbose_name='Название категории')),
                ('subcategory_code', models.CharField(max_length=20, verbose_name='Код подкатегории')),
                ('subcategory_name', models.CharField(max_length=20, verbose_name='Название подкатегории')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField(default=1, unique=True, verbose_name='ID Пользователя')),
                ('name', models.CharField(max_length=100, verbose_name='Имя Пользователя')),
                ('username', models.CharField(max_length=100, verbose_name='Username Пользователя')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usersmanage.user', unique=True)),
                ('referrer_id', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'Реферал',
                'verbose_name_plural': 'Рефералы',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('purchase_time', models.DateTimeField(auto_now_add=True, verbose_name='Время Покупки')),
                ('shipping_address', models.JSONField(null=True, verbose_name='Адрес Доставки')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Номер Телефона')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='Email')),
                ('receiver', models.CharField(max_length=100, verbose_name='Имя Получателя')),
                ('successful', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('buyer', models.ForeignKey(on_delete=models.SET(0), to='usersmanage.user', verbose_name='Покупатель')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersmanage.item', verbose_name='Идентификатор Товара')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
            },
        ),
    ]