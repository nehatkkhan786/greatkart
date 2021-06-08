# Generated by Django 3.2.2 on 2021-06-06 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210606_1757'),
        ('cart', '0002_auto_20210606_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_item_size', to='store.sizes'),
        ),
    ]
