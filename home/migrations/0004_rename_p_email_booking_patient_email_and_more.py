# Generated by Django 4.2.5 on 2024-06-20 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='p_email',
            new_name='patient_email',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='p_name',
            new_name='patient_name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='p_phone',
            new_name='patient_phone',
        ),
    ]