# Generated by Django 3.2.6 on 2021-10-21 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LokalApp', '0007_cartitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product_id',
            new_name='item_code',
        ),
    ]
