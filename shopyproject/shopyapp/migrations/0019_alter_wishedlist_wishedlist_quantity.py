# Generated by Django 4.1.7 on 2023-04-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopyapp', '0018_alter_cart_cartproduct_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishedlist',
            name='wishedlist_quantity',
            field=models.IntegerField(blank=True, default=False, null=True),
        ),
    ]
