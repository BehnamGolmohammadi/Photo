# Generated by Django 3.2.15 on 2022-08-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Category',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]
