# Generated by Django 4.2.3 on 2024-07-07 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_civilstatus_item_civil_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='civil_status',
            new_name='province',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='gender',
            new_name='sexuality',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='nationality',
            new_name='talent',
        ),
    ]
