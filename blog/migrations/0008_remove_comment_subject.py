# Generated by Django 3.2.15 on 2022-08-18 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Subject',
        ),
    ]
