# Generated by Django 4.1.1 on 2022-11-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
