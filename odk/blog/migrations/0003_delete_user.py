# Generated by Django 3.2.12 on 2022-04-24 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220424_1116'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]