# Generated by Django 4.0 on 2021-12-29 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_alter_product_options_product_sorting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=100, verbose_name='Сесия')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=25, verbose_name='Телефон')),
                ('is_cleaning', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='cart.cart', verbose_name='Корзина')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Продукт Заказа',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='cart.cart', verbose_name='Корзина')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Продукт корзины',
                'verbose_name_plural': 'Предметы',
            },
        ),
    ]
