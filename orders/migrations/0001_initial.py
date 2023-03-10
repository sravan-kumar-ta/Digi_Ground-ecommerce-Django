# Generated by Django 4.1.4 on 2023-01-02 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0006_address_is_available_alter_address_pin_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, default=None, max_length=50, null=True, unique=True)),
                ('sub_total', models.FloatField()),
                ('tax', models.FloatField()),
                ('shipping_charge', models.FloatField()),
                ('discount', models.FloatField()),
                ('grand_total', models.FloatField()),
                ('status', models.IntegerField(choices=[(1, 'Order Confirmed'), (2, 'Shipped'), (3, 'Delivered')], default=1)),
                ('datetime_of_payment', models.DateTimeField(default=django.utils.timezone.now)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=150, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=150, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
