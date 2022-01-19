# Generated by Django 4.0 on 2022-01-11 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_galery_sorting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galery',
            options={'ordering': ['sorting'], 'verbose_name': 'Галерея', 'verbose_name_plural': 'Галерея'},
        ),
        migrations.AddField(
            model_name='service',
            name='link',
            field=models.URLField(default='', max_length=100, verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]