# Generated by Django 4.2.6 on 2023-10-31 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0007_alter_phonemodels_image_alter_phonemodels_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodels',
            name='Release_year',
            field=models.IntegerField(null=True),
        ),
    ]
