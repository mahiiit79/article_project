# Generated by Django 5.0.3 on 2024-03-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'verbose_name': 'دسته بندی مقالات', 'verbose_name_plural': 'دسته بندی های مقالات'},
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ انتشار مقاله'),
        ),
    ]
