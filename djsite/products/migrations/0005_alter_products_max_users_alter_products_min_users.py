# Generated by Django 4.2.10 on 2024-02-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_products_alter_access_product_alter_group_product_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="max_users",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="products",
            name="min_users",
            field=models.IntegerField(),
        ),
    ]