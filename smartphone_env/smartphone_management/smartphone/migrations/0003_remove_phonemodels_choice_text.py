# Generated by Django 4.2.6 on 2023-10-30 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0002_alter_brand_created_at_alter_brand_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonemodels',
            name='choice_text',
        ),
    ]
