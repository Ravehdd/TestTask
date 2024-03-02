# Generated by Django 4.2.10 on 2024-02-29 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_product_max_users_product_min_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("start_time", models.DateTimeField(blank=True)),
                ("price", models.FloatField()),
                ("max_users", models.IntegerField(default=10)),
                ("min_users", models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name="access",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="products.products"
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="products.products"
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="products.products"
            ),
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]
