# Generated by Django 2.2.15 on 2020-09-15 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_datecount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datecount',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
