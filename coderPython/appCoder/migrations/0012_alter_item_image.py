# Generated by Django 4.2.5 on 2023-10-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appCoder", "0011_alter_item_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="avatares"),
        ),
    ]