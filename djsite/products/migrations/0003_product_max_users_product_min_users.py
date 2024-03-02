# Generated by Django 4.2.10 on 2024-02-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_remove_product_max_users_remove_product_min_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="max_users",
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name="product",
            name="min_users",
            field=models.IntegerField(default=1),
        ),
    ]
