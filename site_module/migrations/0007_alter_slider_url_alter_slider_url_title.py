# Generated by Django 4.1.1 on 2023-04-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0006_slider_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.CharField(max_length=200, verbose_name='لینک'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url_title',
            field=models.CharField(max_length=200, verbose_name='آدرس'),
        ),
    ]
