# Generated by Django 5.0.3 on 2024-03-09 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_alter_customer_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('FB', 'Painting'), ('NB', 'Sculptures'), ('MB', 'Photography'), ('EC', 'Hand Crafts')], max_length=2),
        ),
    ]
