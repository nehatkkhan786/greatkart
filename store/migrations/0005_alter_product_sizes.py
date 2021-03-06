# Generated by Django 3.2.2 on 2021-06-06 08:40

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_color_product_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Small', 'S'), ('Medium', 'M'), ('Large', 'L')], max_length=20),
        ),
    ]
