# Generated by Django 4.1.4 on 2023-01-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_address_phone_number_alter_address_pin_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='pin_code',
            field=models.PositiveIntegerField(),
        ),
    ]
