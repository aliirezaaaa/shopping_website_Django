# Generated by Django 4.0.3 on 2022-04-08 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='check_sub',
            new_name='sub',
        ),
    ]