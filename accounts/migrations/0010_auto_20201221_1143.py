# Generated by Django 2.2 on 2020-12-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20201221_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripadvisorreviews',
            name='date',
            field=models.TextField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='tripadvisorreviews',
            name='rating',
            field=models.TextField(max_length=800, null=True),
        ),
    ]
