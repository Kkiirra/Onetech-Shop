# Generated by Django 4.0.4 on 2022-05-30 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_product_is_faivorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_faivorite',
        ),
    ]