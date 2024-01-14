# Generated by Django 5.0.1 on 2024-01-14 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_tag_order_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Tags',
        ),
        migrations.AddField(
            model_name='product',
            name='Tags',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
    ]
