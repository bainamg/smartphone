# Generated by Django 4.2.6 on 2023-11-07 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0012_alter_transactions_transaction_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonemodels',
            old_name='is_available',
            new_name='available_number',
        ),
    ]