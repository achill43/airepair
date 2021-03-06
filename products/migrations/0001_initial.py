# Generated by Django 4.0 on 2021-12-10 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('sub_title', models.CharField(max_length=100, verbose_name='Текст')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('image', models.FileField(upload_to='img/products/')),
                ('price', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
