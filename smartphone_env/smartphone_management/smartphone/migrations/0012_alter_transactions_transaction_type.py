# Generated by Django 4.2.6 on 2023-11-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0011_alter_transactions_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Transaction_type',
            field=models.CharField(blank=True, choices=[('Card', '1'), ('Cash', '2')], max_length=200, null=True),
        ),
    ]