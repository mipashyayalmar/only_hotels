# Generated by Django 4.2.2 on 2024-10-14 08:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Advertise",
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
                ("name", models.CharField(max_length=200)),
                ("image2", models.ImageField(default="", upload_to="shop/advertise/")),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("msg_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(default="", max_length=70)),
                ("phone", models.CharField(default="", max_length=70)),
                ("desc", models.CharField(default="", max_length=500)),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                ("items_json", models.CharField(max_length=5000)),
                ("userId", models.IntegerField(default=0)),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("name", models.CharField(blank=True, max_length=90, null=True)),
                ("email", models.CharField(blank=True, max_length=111, null=True)),
                ("address", models.CharField(blank=True, max_length=111, null=True)),
                ("city", models.CharField(blank=True, max_length=111, null=True)),
                ("state", models.CharField(blank=True, max_length=111, null=True)),
                ("zip_code", models.CharField(blank=True, max_length=111, null=True)),
                (
                    "phone",
                    models.CharField(blank=True, default="", max_length=111, null=True),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("cash", "Cash"),
                            ("card", "Card"),
                            ("online", "Online"),
                            ("other", "Other"),
                        ],
                        default="cash",
                        max_length=10,
                    ),
                ),
                (
                    "payment_comments",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="OrderUpdate",
            fields=[
                ("update_id", models.AutoField(primary_key=True, serialize=False)),
                ("order_id", models.IntegerField(default="")),
                ("update_desc", models.CharField(max_length=5000)),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("product_name", models.CharField(max_length=50)),
                ("category", models.CharField(default="", max_length=50)),
                ("subcategory", models.CharField(default="", max_length=50)),
                ("price", models.IntegerField(default=0)),
                ("desc", models.CharField(max_length=200)),
                ("pub_date", models.DateField()),
                ("image", models.ImageField(default="", upload_to="shop/images")),
            ],
        ),
        migrations.CreateModel(
            name="Table",
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
                ("number", models.PositiveIntegerField(unique=True)),
                ("status", models.CharField(default="Blank", max_length=20)),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
            ],
        ),
    ]
