# Generated by Django 5.1.5 on 2025-02-01 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_faq_rename_adress_contactmodel_address'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactModel',
        ),
    ]
