# Generated by Django 3.1.3 on 2020-12-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_auto_20201205_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]
