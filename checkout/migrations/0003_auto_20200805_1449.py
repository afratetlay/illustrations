# Generated by Django 3.0.8 on 2020-08-05 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_orderlineitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(default='illustrations', on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.Order'),
        ),
    ]
