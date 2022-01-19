# Generated by Django 4.0 on 2022-01-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/reviews/', verbose_name='Изображение')),
                ('sorting', models.PositiveIntegerField(default=0, verbose_name='Сортировка')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['sorting'],
            },
        ),
    ]