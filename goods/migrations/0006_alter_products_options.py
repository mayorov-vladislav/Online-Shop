# Generated by Django 4.2.7 on 2024-04-04 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_alter_products_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',), 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]