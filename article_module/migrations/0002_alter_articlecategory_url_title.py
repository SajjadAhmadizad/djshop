# Generated by Django 4.1.1 on 2023-05-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='url_title',
            field=models.CharField(max_length=100, unique=True, verbose_name='عنوان در url'),
        ),
    ]
