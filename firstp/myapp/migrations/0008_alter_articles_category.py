# Generated by Django 4.0.2 on 2022-02-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_articles_category_alter_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='myapp.Category', verbose_name='دسته بندی ها'),
        ),
    ]
