# Generated by Django 4.1.1 on 2023-03-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'تصویر آپلود شده', 'verbose_name_plural': 'لیست تصاویر آپلود شده'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='تصویر آپلود شده'),
        ),
    ]
