# Generated by Django 3.0.8 on 2020-08-07 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20200805_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default=1, editable=False, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.Order'),
        ),
    ]