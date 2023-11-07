# Generated by Django 4.2.6 on 2023-11-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted')], default='pending', max_length=10),
        ),
    ]
