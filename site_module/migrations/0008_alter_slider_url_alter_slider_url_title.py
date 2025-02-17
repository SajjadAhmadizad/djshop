# Generated by Django 4.1.1 on 2023-05-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0007_alter_slider_url_alter_slider_url_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.URLField(max_length=2000, verbose_name='لینک'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url_title',
            field=models.CharField(max_length=200, verbose_name='متن نمایش لینک'),
        ),
    ]
