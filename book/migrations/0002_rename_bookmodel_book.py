# Generated by Django 3.2.6 on 2021-08-22 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookModel',
            new_name='Book',
        ),
    ]